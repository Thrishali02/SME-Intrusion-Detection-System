# SME Intrusion Detection and Log Analysis System

Developed as part of a final year research project.
This project presents a cost-effective cybersecurity monitoring framework designed for Small and Medium-sized Enterprises (SMEs).

## Overview

The system uses a honeypot (Cowrie) to detect unauthorized access attempts and transforms raw intrusion data into simple, understandable security reports.

## Features

- Intrusion detection using a honeypot
- Logging of attacker activities
- Python-based log analysis
- Visualization of attack patterns
- Automated PDF report generation

## Technologies Used

- Python
- Cowrie Honeypot
- Hydra (for attack simulation)
- Matplotlib
- ReportLab

## System Workflow

1. Intrusion attempts are captured using the honeypot
2. Logs are stored in JSON format
3. Python scripts analyze intrusion data
4. Graphs and summaries are generated
5. A PDF report is created for SME users

## Files Included

- analyze_logs.py → Log analysis
- visualize.py → Graph generation
- generate_report.py → PDF report creation
- cowrie_sample.json → Sample log data

## Purpose

This system helps SMEs understand cybersecurity threats without needing advanced technical knowledge.

## Note

This project was developed in a controlled virtual environment for academic purposes.
This project demonstrates SME-friendly cybersecurity reporting.
Includes detailed attack records, visualization, and SME-focused reporting.
