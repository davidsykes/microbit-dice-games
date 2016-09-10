cat testprefix.py > testcode.py
cat code.py >> testcode.py
python3 -m unittest discover
