# Copyright (C) 2020 - 2021 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

class ResolveTracker:

    def __init__(self):
        self._ip_map = {}
        self._domain_map = {}

    def find_domains(self, ip):
        return list(self._domain_map.get(ip, set()))

    def find_ips(self, domain):
        return list(self._ip_map.get(domain, set()))

    def find_domain_all(self, domain):
        all = set()
        for entry in self._domain_map.keys():
            if entry.endswith(domain):
                all.add(entry)

        return list(all)

    def add_resolved(self, domain, ip):
        self._domain_map.setdefault(domain, set()).add(ip)
        self._ip_map.setdefault(ip, set()).add(domain)
