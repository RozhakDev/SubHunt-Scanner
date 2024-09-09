import argparse
import logging
from pathlib import Path

from subhunt.finder import SubdomainFinder
from subhunt.logger import setup_logger
from subhunt.config import HEADERS

def main():
    """
    Main function to run the SubHunt tool.
    Parses command-line arguments, sets up logging, and initiates the subdomain search.
    """
    parser = argparse.ArgumentParser(
        description="SubHunt: A professional subdomain finder for ethical hacking education.",
        epilog="Example: python main.py -d example.com -o results.txt --complete"
    )
    parser.add_argument(
        "-d", "--domain",
        required=True,
        help="The target domain to scan for subdomains (e.g., example.com)."
    )
    parser.add_argument(
        "-o", "--output",
        help="Optional: The file path to save the found subdomains."
    )
    parser.add_argument(
        "--complete",
        action="store_true",
        help="Perform a complete scan, including expired certificates. Default is a quick scan."
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging to the console."
    )
    args = parser.parse_args()

    log_level = logging.DEBUG if args.verbose else logging.INFO
    logger = setup_logger(log_level=log_level)
    logger.info("SubHunt application started.")
    logger.debug("Arguments parsed: %s", args)

    try:
        finder = SubdomainFinder(
            domain=args.domain,
            headers=HEADERS,
            complete_scan=args.complete
        )
        subdomains = finder.discover()

        if not subdomains:
            logger.warning("No subdomains found for the domain: %s", args.domain)
            return

        logger.info("Successfully found %d subdomains for %s.", len(subdomains), args.domain)

        for subdomain in sorted(list(subdomains)):
            logger.info("Found: %s", subdomain)

        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with output_path.open('w', encoding='utf-8') as f:
                for subdomain in sorted(list(subdomains)):
                    f.write(f"{subdomain}\n")
            logger.info("Results successfully saved to: %s", args.output)
    except (ValueError, ConnectionError) as e:
        logger.error("An error occurred: %s", e)
    except Exception as e:
        logger.critical("An unexpected critical error occurred: %s", e, exc_info=True)
    finally:
        logger.info("SubHunt application finished.")

if __name__ == "__main__":
    main()