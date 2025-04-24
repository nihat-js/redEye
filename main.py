from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import datetime
import json

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Change this to a secure key in production

# Default users for demo
USERS = {
    "admin": {"password": "admin", "role": "admin"},
    "pentester1": {"password": "test123", "role": "user"},
    "pentester2": {"password": "test456", "role": "user"},
    "pentester3": {"password": "test789", "role": "user"},
    "pentester4": {"password": "test000", "role": "user"}
}

# Mock data (from original code)
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
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in USERS and USERS[username]["password"] == password:
            session['username'] = username
            session['role'] = USERS[username]["role"]
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/dashboard')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('index.html', data=mock_data)

@app.route('/enumeration')
def enumeration():
    if 'username' in session:
        return render_template('enumeration.html', data=mock_data['enumeration'])
    return redirect(url_for('login'))

@app.route('/privilege-escalation')
def privilege_escalation():
    if 'username' in session:
        return render_template('privilege_escalation.html', data=mock_data['privilege_escalation'])
    return redirect(url_for('login'))

@app.route('/exploitation')
def exploitation():
    if 'username' in session:
        return render_template('exploitation.html', data=mock_data['exploitation'])
    return redirect(url_for('login'))

@app.route('/active-directory')
def active_directory():
    if 'username' in session:
        return render_template('active-directory.html', data=mock_data['active_directory'])
    return redirect(url_for('login'))

@app.route('/scripts')
def scripts():
    if 'username' in session:
        return render_template('scripts.html')
    return redirect(url_for('login'))

@app.route('/handler')
def handler():
    if 'username' in session:
        return render_template('handler.html')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)