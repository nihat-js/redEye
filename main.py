
from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json

app = Flask(__name__)

# Mock data
mock_data = {
    'enumeration': {
        'live_hosts': ['192.168.1.100', '192.168.1.101', '192.168.1.102'],
        'open_ports': {
            '192.168.1.100': [80, 443, 22],
            '192.168.1.101': [21, 80, 3389],
        },
        'services': ['HTTP', 'SSH', 'RDP', 'FTP'],
        'shares': ['\\\\SERVER\\Public', '\\\\SERVER\\Data'],
    },
    'privilege_escalation': {
        'vulnerable_services': ['spoolsv.exe', 'unquoted_service.exe'],
        'weak_permissions': ['/etc/shadow', 'C:\\Program Files\\Vulnerable App'],
        'risky_programs': ['sudo', 'winlogon.exe'],
        'severity_counts': {'High': 3, 'Medium': 5, 'Low': 2}
    },
    'exploitation': {
        'successful_exploits': [
            {'target': '192.168.1.100', 'method': 'MS17-010', 'status': 'Success'},
            {'target': '192.168.1.101', 'method': 'CVE-2021-44228', 'status': 'Success'},
        ],
        'active_sessions': 2,
        'payloads_delivered': 5
    },
    'active_directory': {
        'users': ['Administrator', 'Guest', 'jsmith', 'awhite'],
        'groups': ['Domain Admins', 'Enterprise Admins', 'Users'],
        'domain_info': {
            'name': 'CORP.LOCAL',
            'trust_relationships': ['EXTERNAL.COM', 'PARTNER.COM']
        }
    }
}

@app.route('/')
def index():
    return render_template('index.html', data=mock_data)

@app.route('/enumeration')
def enumeration():
    return render_template('enumeration.html', data=mock_data['enumeration'])

@app.route('/privilege-escalation')
def privilege_escalation():
    return render_template('privilege_escalation.html', data=mock_data['privilege_escalation'])

@app.route('/exploitation')
def exploitation():
    return render_template('exploitation.html', data=mock_data['exploitation'])

@app.route('/active-directory')
def active_directory():
    return render_template('active_directory.html', data=mock_data['active_directory'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
