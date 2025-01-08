#!/usr/bin/env python

import json
import sys

def main():
    inventory = {
        "_meta": {
            "hostvars": {
                "controlplane": {
                    "ansible_python_interpreter": sys.executable
                },
                "node1": {
                    "ansible_python_interpreter": sys.executable
                },
                "node2": {
                    "ansible_python_interpreter": sys.executable
                }
            }
        },
        "all": {
            "children": ["ungrouped", "controlplane", "workers"]
        },
        "controlplane": {
            "hosts": ["controlplane"]
        },
        "workers": {
            "hosts": ["node1", "node2"]
        }
    }

    print(json.dumps(inventory, indent=2))

if __name__ == "__main__":
    main()
