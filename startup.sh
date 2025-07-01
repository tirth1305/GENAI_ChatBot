#!/bin/bash
chmod +x startup.sh
streamlit run ChatBot.py --server.port=8000 --server.address=0.0.0.0
