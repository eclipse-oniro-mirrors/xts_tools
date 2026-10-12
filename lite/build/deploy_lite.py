#!/usr/bin/env python3
import argparse
import json
import os
import shutil
import sys
import stat


def deploy_test_json(src, dst, kernel_type):
    """Copy Test.json to the output directory, injecting the build kernel
    type into the MountKit 'type_kernel' field so the deployed config always
    matches the kernel this suite was built for."""
    type_value = "lite" if kernel_type == "liteos_a" else "linux"
    with open(src, "r", encoding="utf-8") as file_handle:
        config = json.load(file_handle)
    for kit in config.get("kits", []):
        if kit.get("type") == "MountKit":
            kit["type_kernel"] = type_value
    with open(dst, "w", encoding="utf-8") as file_handle:
        json.dump(config, file_handle, indent=4, ensure_ascii=False)
        file_handle.write("\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hap", required=True)
    parser.add_argument("--hap-out", required=True)
    parser.add_argument("--test-json", required=False)
    parser.add_argument("--test-json-out", required=False)
    parser.add_argument("--aa-src", required=False)
    parser.add_argument("--tools-out", required=False)
    parser.add_argument("--kernel-type", required=False)
    args = parser.parse_args()

    os.makedirs(args.hap_out, exist_ok=True)
    shutil.copy2(args.hap, args.hap_out)

    if args.test_json and args.test_json_out:
        os.makedirs(os.path.dirname(args.test_json_out), exist_ok=True)
        if args.kernel_type:
            deploy_test_json(args.test_json, args.test_json_out, args.kernel_type)
        else:
            shutil.copy2(args.test_json, args.test_json_out)

    if args.aa_src and args.tools_out and os.path.isfile(args.aa_src):
        os.makedirs(args.tools_out, exist_ok=True)
        dst = os.path.join(args.tools_out, "aa")
        shutil.copy2(args.aa_src, dst)
        os.chmod(dst, os.stat(dst).st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)

    return 0


if __name__ == "__main__":
    sys.exit(main())
