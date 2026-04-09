# Sales Data Visualizer (OOP Architecture)

### 🚀 Project Overview
A robust data processing tool built to master **Object-Oriented Programming (OOP)**. It reads sales data from multiple formats (TXT, JSON) and generates interactive visual reports.

### 🛠️ Key Technical Features
- **Abstract Base Classes (ABC)**: Enforced a strict interface for file readers.
- **Polymorphism**: Unified data processing logic regardless of source format.
- **Composition**: Decoupled the `DataProducer` from specific reader implementations.
- **Encapsulation**: Protected sensitive attributes using private members.

### 📂 Structure
- `data/`: Raw sales datasets.
- `test.py`: Core logic and Pyecharts implementation.
