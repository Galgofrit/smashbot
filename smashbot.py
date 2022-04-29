import sys
import collections
import argparse
import logging
import vgamepad
import pprint
import time

FRAME_RATE = 1/60 # 60 FPS

Key = collections.namedtuple('Key', ['name', 'code']) # Store controller button mappings with description

# Key mapping
class KEYS:
    SHIELD = Key('shield', vgamepad.DS4_BUTTONS.DS4_BUTTON_TRIGGER_RIGHT)


# Logger
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt="%H:%M:%S",
)

def alternate_key_state():
    while True:
        yield True
        yield False

def run_bot(gamepad, randomize_di, spam_keys):
    alternator = alternate_key_state()

    try:
        while True: # Main program loop
            alternate_mode = next(alternator)

            for key in spam_keys:
                if alternate_mode:
                    logger.debug(f'Holding key \'{key.name}\'.')
                    gamepad.press_button(button=key.code)
                else:
                    logger.debug(f'Releasing key \'{key.name}\'.')
                    gamepad.release_button(button=key.code) 

            gamepad.update()
            time.sleep(FRAME_RATE)

    except KeyboardInterrupt:
        logger.info('Stopping.')
        return


def main():
    parser = argparse.ArgumentParser(description='Run smash bot for practicing.')
    parser.add_argument('-s', '--spam-shield', action='store_true', default=False, help='spam shield and airdodge')
    parser.add_argument('-di', '--randomize-di', action='store_true', default=False, help='randomize DI')
    parser.add_argument('-dbg', '--debug', action='store_true', default=False, help='run in debug mode')

    args = parser.parse_args()

    spam_keys = []

    if args.spam_shield:
        spam_keys.append(KEYS.SHIELD)

    if args.debug:
        logger.setLevel(logging.DEBUG)
        logger.debug('Running in DEBUG mode')

    logger.info(f'Starting up. Configuration: randomize_di={args.randomize_di},\
            \n\tspam_keys={pprint.pformat(spam_keys)}')

    logger.info('Creating gamepad...')
    gamepad = vgamepad.VDS4Gamepad()

    if not gamepad:
        logger.error('Could not create gamepad.')
        return -2

    logger.info('Gamepad created.')
    logger.info('Starting bot. Stop at any time with Ctrl+C.')

    run_bot(gamepad, args.randomize_di, spam_keys)

    logger.info('Removing gamepad...')
    del gamepad
    logger.info('Finished.')

    return 0


if __name__=='__main__':
    sys.exit(main())
