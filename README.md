David Ngige

ITMS 543

09/07/2021

# s1mpleRec0n - Basic Port Scanners

#### How to use

**Python**

```txt
# Install requirements
pip3 -r requirements.txt

# running script
➜ python3 simpleRecon.py             
  ^    ^    ^    ^    ^    ^    ^    ^    ^    ^    ^  
 /s\  /1\  /m\  /p\  /l\  /e\  /R\  /e\  /c\  /0\  /n\ 
<___><___><___><___><___><___><___><___><___><___><___>

============================================================
Enter target IP to scan: scanme.nmap.org
============================================================
Performing port scan on scanme.nmap.org
============================================================
Port	Service	Status
22		ssh		Open
80		http	Open
============================================================
Scan complete
============================================================
```

**Bash Script**

```txt
# give file executing persmissions
chmod +x ./simpleRecon

# run file
➜./simpleRecon -i scanme.nmap.org

            _              _ __     _              ___                                   
   ___     (_)    _ __    | '_ \   | |     ___    | _ \    ___     __      ___    _ _    
  (_-<     | |   | '  \   | .__/   | |    / -_)   |   /   / -_)   / _|    / _ \  | ' \   
  /__/_   _|_|_  |_|_|_|  |_|__   _|_|_   \___|   |_|_\   \___|   \__|_   \___/  |_||_|  
_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-D-0-'"`-N-0-'"`-G-0-'"`-I-0-'"`-G-0-'"`-E-0-' 
=================================
Scanning: scanme.nmap.org
=================================
Port 22 is open
Port 80 is open
=================================
Scan complete.
=================================
```