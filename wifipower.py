import asyncio
import argparse
from winrt.windows.devices import radios


async def wifipower(turn_on):
    all_radios = await radios.Radio.get_radios_async()
    for this_radio in all_radios:
        if this_radio.kind == radios.RadioKind.WI_FI:
            if turn_on:
                result = await this_radio.set_state_async(radios.RadioState.ON)
            else:
                result = await this_radio.set_state_async(radios.RadioState.OFF)


if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument(
        "-o",
        "--off",
        help="disalbe bluetooth device default will be on",
        action="store_true",
    )
    args = parse.parse_args()
    if args.off:
        asyncio.run(wifipower(False))
    else:
        asyncio.run(wifipower(True))
