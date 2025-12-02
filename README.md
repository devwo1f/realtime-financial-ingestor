# Real-Time Crypto Data Pipeline

## Project Overview
This project is a data engineering pipeline that streams real-time cryptocurrency trade data (Bitcoin, Ethereum) from the Coinbase WebSocket API. It ingests the live data stream, normalizes the format, and loads it into a storage system for analysis.

The main focus of this project is **fault tolerance**. The system includes robust error handling to manage network instability, ensuring that the pipeline automatically reconnects and resumes data collection without manual intervention.

## Tech Stack
* **Language:** Python 3.9+
* **Source:** Coinbase WebSocket API (Public Feed)
* **Ingestion:** Python `websocket-client`
* **Storage:** Local CSV / SQLite (Scalable to AWS S3/Redshift)
* **Libraries:** `pandas`, `json`, `logging`

## Key Features
1.  **Real-Time Ingestion:** Low-latency streaming of trade data using WebSockets.
2.  **Auto-Recovery:** Custom logic to detect connection drops and automatically reconnect using an exponential backoff strategy.
3.  **Data Validation:** Checks incoming JSON messages for required fields before processing.

## How to Run
1.  Clone the repository:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/crypto-pipeline.git](https://github.com/YOUR_USERNAME/crypto-pipeline.git)
    ```
2.  Install dependencies:
    ```bash
    pip install websocket-client pandas
    ```
3.  Run the pipeline:
    ```bash
    python pipeline.py
    ```
