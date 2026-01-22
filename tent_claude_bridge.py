from flask import Flask, request, jsonify
import hashlib, json, os
PRIMES = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73]
app = Flask(__name__)
@app.route('/query', methods=['POST'])
def query():
    t = request.get_json().get('query','')
    h = hashlib.sha256(t.encode()).hexdigest()
    b21 = [int(h[i:i+2],16)%21 for i in range(0,16,2)]
    return jsonify({"query":t, "base21":b21, "primes":[PRIMES[d%len(PRIMES)] for d in b21]})
@app.route('/status')
def status():
    n,l = 0,0
    if os.path.exists("universal_prime_graph.json"):
        with open("universal_prime_graph.json") as f: d=json.load(f); n,l=len(d.get("nodes",{})),len(d.get("ledger",[]))
    return jsonify({"bridge":"ONLINE","nodes":n,"ledger":l})
if __name__ == "__main__": app.run(port=5000)
