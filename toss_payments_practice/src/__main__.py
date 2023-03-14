from flask import Flask, request, jsonify, render_template
from app import server




if __name__ == "__main__":
    server.run(port=5009)