from typing import Generator, KeysView

SERVICES_FOR_GROUP = {
    "all": "coffee_harvester coffee_timelord_launcher coffee_timelord coffee_farmer coffee_full_node coffee_wallet".split(),
    "node": "coffee_full_node".split(),
    "harvester": "coffee_harvester".split(),
    "farmer": "coffee_harvester coffee_farmer coffee_full_node coffee_wallet".split(),
    "farmer-no-wallet": "coffee_harvester coffee_farmer coffee_full_node".split(),
    "farmer-only": "coffee_farmer".split(),
    "timelord": "coffee_timelord_launcher coffee_timelord coffee_full_node".split(),
    "timelord-only": "coffee_timelord".split(),
    "timelord-launcher-only": "coffee_timelord_launcher".split(),
    "wallet": "coffee_wallet coffee_full_node".split(),
    "wallet-only": "coffee_wallet".split(),
    "introducer": "coffee_introducer".split(),
    "simulator": "coffee_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
