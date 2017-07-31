#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter04/dns_mx.py
# Looking up a mail domain - the part of an email address after the `@`

import argparse, dns.resolver

def resolve_hostname(hostname):
    print('Not implemented ....')
    return

def resolve_email_domain(domain):
    "For an email address `name@domain` find its mail server IP addresses"
    try:
        answer = dns.resolver.query(domain, 'MX', raise_on_no_answer=False)
    except dns.resolver.NXDOMAIN:
        print('Error: no such domain', domain)
        return
    if answer.rrset is not None:
        records = sorted(answer, key=lambda record: record.preference)
        for record in records:
            name = record.exchange.to_text(omit_final_dot=True)
            print('Priority:', record.preference, 'Name:', name)
    else:
        print('This domain has no explicit MX records')
        print('Attempting to resolve it as an A, AAAA, or CNAME')
        resolve_hostname(domain)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find mailserver IP address')
    parser.add_argument('domain', help='domain that you want send mail to')
    resolve_email_domain(parser.parse_args().domain)
