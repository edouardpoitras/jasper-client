# -*- coding: utf-8 -*-
import sys
import logging
import argparse

from . import application


def main(args=None):
    parser = argparse.ArgumentParser(description='Jasper Voice Control Center')
    parser.add_argument('--local', action='store_true',
                        help='Use text input instead of a real microphone')
    parser.add_argument('--debug', action='store_true',
                        help='Show debug messages')
    list_info = parser.add_mutually_exclusive_group(required=False)
    list_info.add_argument('--list-plugins', action='store_true',
                           help='List plugins and exit')
    list_info.add_argument('--list-audio-devices', action='store_true',
                           help='List audio devices and exit')
    p_args = parser.parse_args(args)

    print("*******************************************************")
    print("*             JASPER - THE TALKING COMPUTER           *")
    print("* (c) 2015 Shubhro Saha, Charlie Marsh & Jan Holthuis *")
    print("*******************************************************")

    # Set up logging
    logging.basicConfig(level=logging.DEBUG if p_args.debug else logging.INFO)

    # Run Jasper
    app = application.Jasper(use_local_mic=p_args.local)
    if p_args.list_plugins:
        app.list_plugins()
        sys.exit(1)
    elif p_args.list_audio_devices:
        app.list_audio_devices()
        sys.exit(0)
    app.run()


if __name__ == '__main__':
    main()
