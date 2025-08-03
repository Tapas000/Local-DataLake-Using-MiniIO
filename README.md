# 🗂️ Local Data Lake with MinIO

This project sets up a **local data lake** using **MinIO**, an open-source, S3-compatible object storage system. It allows you to store and organize files like CSVs, JSON, images, videos, and PDFs via a web interface or Python scripts.

---

## 📁 Features

- 🐳 Dockerized MinIO server
- ✅ Web-based UI for managing files
- 🐍 Python script to auto-upload files
- 📦 Supports all file types (structured, semi-structured, unstructured)

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/local-minio-datalake.git
cd local-minio-datalake


🧰 Tools Used
MinIO
Docker
boto3 (Python SDK for S3)

1. run docker-compose  up -d
2. pip install boto3
3. upload Any data in any format 
4. run python upload_sample.py
