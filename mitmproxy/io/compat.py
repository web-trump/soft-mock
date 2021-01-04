"""
This module handles the import of mitmproxy flows generated by old versions.

The flow file version is decoupled from the mitmproxy release cycle (since
v3.0.0dev) and versioning. Every change or migration gets a new flow file
version number, this prevents issues with developer builds and snapshots.
"""
import uuid
from typing import Any, Dict, Mapping, Union  # noqa

from mitmproxy import version
from mitmproxy.utils import strutils


def convert_011_012(data):
    data[b"version"] = (0, 12)
    return data


def convert_012_013(data):
    data[b"version"] = (0, 13)
    return data


def convert_013_014(data):
    data[b"request"][b"first_line_format"] = data[b"request"].pop(b"form_in")
    data[b"request"][b"http_version"] = b"HTTP/" + ".".join(
        str(x) for x in data[b"request"].pop(b"httpversion")).encode()
    data[b"response"][b"http_version"] = b"HTTP/" + ".".join(
        str(x) for x in data[b"response"].pop(b"httpversion")).encode()
    data[b"response"][b"status_code"] = data[b"response"].pop(b"code")
    data[b"response"][b"body"] = data[b"response"].pop(b"content")
    data[b"server_conn"].pop(b"state")
    data[b"server_conn"][b"via"] = None
    data[b"version"] = (0, 14)
    return data


def convert_014_015(data):
    data[b"version"] = (0, 15)
    return data


def convert_015_016(data):
    for m in (b"request", b"response"):
        if b"body" in data[m]:
            data[m][b"content"] = data[m].pop(b"body")
    if b"msg" in data[b"response"]:
        data[b"response"][b"reason"] = data[b"response"].pop(b"msg")
    data[b"request"].pop(b"form_out", None)
    data[b"version"] = (0, 16)
    return data


def convert_016_017(data):
    data[b"server_conn"][b"peer_address"] = None
    data[b"version"] = (0, 17)
    return data


def convert_017_018(data):
    # convert_unicode needs to be called for every dual release and the first py3-only release
    data = convert_unicode(data)

    data["server_conn"]["ip_address"] = data["server_conn"].pop("peer_address", None)
    data["marked"] = False
    data["version"] = (0, 18)
    return data


def convert_018_019(data):
    # convert_unicode needs to be called for every dual release and the first py3-only release
    data = convert_unicode(data)

    data["request"].pop("stickyauth", None)
    data["request"].pop("stickycookie", None)
    data["client_conn"]["sni"] = None
    data["client_conn"]["alpn_proto_negotiated"] = None
    data["client_conn"]["cipher_name"] = None
    data["client_conn"]["tls_version"] = None
    data["server_conn"]["alpn_proto_negotiated"] = None
    if data["server_conn"]["via"]:
        data["server_conn"]["via"]["alpn_proto_negotiated"] = None
    data["mode"] = "regular"
    data["metadata"] = dict()
    data["version"] = (0, 19)
    return data


def convert_019_100(data):
    # convert_unicode needs to be called for every dual release and the first py3-only release
    data = convert_unicode(data)

    data["version"] = (1, 0, 0)
    return data


def convert_100_200(data):
    data["version"] = (2, 0, 0)
    data["client_conn"]["address"] = data["client_conn"]["address"]["address"]
    data["server_conn"]["address"] = data["server_conn"]["address"]["address"]
    data["server_conn"]["source_address"] = data["server_conn"]["source_address"]["address"]
    if data["server_conn"]["ip_address"]:
        data["server_conn"]["ip_address"] = data["server_conn"]["ip_address"]["address"]

    if data["server_conn"]["via"]:
        data["server_conn"]["via"]["address"] = data["server_conn"]["via"]["address"]["address"]
        data["server_conn"]["via"]["source_address"] = data["server_conn"]["via"]["source_address"]["address"]
        if data["server_conn"]["via"]["ip_address"]:
            data["server_conn"]["via"]["ip_address"] = data["server_conn"]["via"]["ip_address"]["address"]

    return data


def convert_200_300(data):
    data["version"] = (3, 0, 0)
    data["client_conn"]["mitmcert"] = None
    data["server_conn"]["tls_version"] = None
    if data["server_conn"]["via"]:
        data["server_conn"]["via"]["tls_version"] = None
    return data


def convert_300_4(data):
    data["version"] = 4
    # This is an empty migration to transition to the new versioning scheme.
    return data


client_connections: Mapping[str, str] = {}
server_connections: Mapping[str, str] = {}


def convert_4_5(data):
    data["version"] = 5
    client_conn_key = (
        data["client_conn"]["timestamp_start"],
        *data["client_conn"]["address"]
    )
    server_conn_key = (
        data["server_conn"]["timestamp_start"],
        *data["server_conn"]["source_address"]
    )
    data["client_conn"]["id"] = client_connections.setdefault(client_conn_key, str(uuid.uuid4()))
    data["server_conn"]["id"] = server_connections.setdefault(server_conn_key, str(uuid.uuid4()))

    if data["server_conn"]["via"]:
        server_conn_key = (
            data["server_conn"]["via"]["timestamp_start"],
            *data["server_conn"]["via"]["source_address"]
        )
        data["server_conn"]["via"]["id"] = server_connections.setdefault(server_conn_key, str(uuid.uuid4()))

    return data


def convert_5_6(data):
    data["version"] = 6
    data["client_conn"]["tls_established"] = data["client_conn"].pop("ssl_established")
    data["client_conn"]["timestamp_tls_setup"] = data["client_conn"].pop("timestamp_ssl_setup")
    data["server_conn"]["tls_established"] = data["server_conn"].pop("ssl_established")
    data["server_conn"]["timestamp_tls_setup"] = data["server_conn"].pop("timestamp_ssl_setup")
    if data["server_conn"]["via"]:
        data["server_conn"]["via"]["tls_established"] = data["server_conn"]["via"].pop("ssl_established")
        data["server_conn"]["via"]["timestamp_tls_setup"] = data["server_conn"]["via"].pop("timestamp_ssl_setup")
    return data


def convert_6_7(data):
    data["version"] = 7
    data["client_conn"]["tls_extensions"] = None
    return data


def convert_7_8(data):
    data["version"] = 8
    data["request"]["trailers"] = None
    if data["response"] is not None:
        data["response"]["trailers"] = None
    return data


def convert_8_9(data):
    data["version"] = 9
    data["request"].pop("first_line_format")
    data["request"]["authority"] = b""
    is_request_replay = data["request"].pop("is_replay", False)
    is_response_replay = False
    if data["response"] is not None:
        is_response_replay = data["response"].pop("is_replay", False)
    if is_request_replay:  # pragma: no cover
        data["is_replay"] = "request"
    elif is_response_replay:  # pragma: no cover
        data["is_replay"] = "response"
    else:
        data["is_replay"] = None
    return data


def convert_9_10(data):
    data["version"] = 10

    def conv_conn(conn):
        conn["state"] = 0
        conn["error"] = None
        conn["tls"] = conn["tls_established"]
        alpn = conn["alpn_proto_negotiated"]
        conn["alpn_offers"] = [alpn] if alpn else None
        cipher = conn["cipher_name"]
        conn["cipher_list"] = [cipher] if cipher else None

    def conv_cconn(conn):
        conn["sockname"] = ("", 0)
        cc = conn.pop("clientcert", None)
        conn["certificate_list"] = [cc] if cc else []
        conv_conn(conn)

    def conv_sconn(conn):
        crt = conn.pop("cert", None)
        conn["certificate_list"] = [crt] if crt else []
        conn["cipher_name"] = None
        conn["via2"] = None
        conv_conn(conn)

    conv_cconn(data["client_conn"])
    conv_sconn(data["server_conn"])
    if data["server_conn"]["via"]:
        conv_sconn(data["server_conn"]["via"])

    return data


def _convert_dict_keys(o: Any) -> Any:
    if isinstance(o, dict):
        return {strutils.always_str(k): _convert_dict_keys(v) for k, v in o.items()}
    else:
        return o


def _convert_dict_vals(o: dict, values_to_convert: dict) -> dict:
    for k, v in values_to_convert.items():
        if not o or k not in o:
            continue  # pragma: no cover
        if v is True:
            o[k] = strutils.always_str(o[k])
        else:
            _convert_dict_vals(o[k], v)
    return o


def convert_unicode(data: dict) -> dict:
    """
    This method converts between Python 3 and Python 2 dumpfiles.
    """
    data = _convert_dict_keys(data)
    data = _convert_dict_vals(
        data, {
            "type": True,
            "id": True,
            "request": {
                "first_line_format": True
            },
            "error": {
                "msg": True
            }
        }
    )
    return data


converters = {
    (0, 11): convert_011_012,
    (0, 12): convert_012_013,
    (0, 13): convert_013_014,
    (0, 14): convert_014_015,
    (0, 15): convert_015_016,
    (0, 16): convert_016_017,
    (0, 17): convert_017_018,
    (0, 18): convert_018_019,
    (0, 19): convert_019_100,
    (1, 0): convert_100_200,
    (2, 0): convert_200_300,
    (3, 0): convert_300_4,
    4: convert_4_5,
    5: convert_5_6,
    6: convert_6_7,
    7: convert_7_8,
    8: convert_8_9,
    9: convert_9_10,
}


def migrate_flow(flow_data: Dict[Union[bytes, str], Any]) -> Dict[Union[bytes, str], Any]:
    while True:
        flow_version = flow_data.get(b"version", flow_data.get("version"))

        # Historically, we used the mitmproxy minor version tuple as the flow format version.
        if not isinstance(flow_version, int):
            flow_version = tuple(flow_version)[:2]

        if flow_version == version.FLOW_FORMAT_VERSION:
            break
        elif flow_version in converters:
            flow_data = converters[flow_version](flow_data)
        else:
            should_upgrade = (
                    isinstance(flow_version, int)
                    and flow_version > version.FLOW_FORMAT_VERSION
            )
            raise ValueError(
                "{} cannot read files with flow format version {}{}.".format(
                    version.MITMPROXY,
                    flow_version,
                    ", please update mitmproxy" if should_upgrade else ""
                )
            )
    return flow_data
