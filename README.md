# 🧬 Bioinformatics Toolkit

A web-based DNA sequence analysis tool built with **Streamlit** and **Biopython**. This toolkit provides an accessible interface for performing essential genomic calculations and sequence manipulations.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 📌 Features

### Core DNA Analysis Tools
*   **GC Content Calculator**: Computes the ratio of Guanine (G) and Cytosine (C) in a DNA sequence.
*   **Complement Generator**: Generates the complementary DNA strand (A↔T, G↔C).
*   **RNA Transcription**: Converts DNA sequences into RNA by replacing Thymine (T) with Uracil (U).
*   **Amino Acid Translation**: Translates DNA into protein sequences using the standard genetic code.
*   **Sequence Alignment**: Performs global sequence alignment using the Needleman-Wunsch algorithm via Biopython.

---

## 🚀 Quick Start

### Prerequisites
*   Python 3.8 or higher
*   pip package manager

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/mehmeterkann/bioinformatics-toolkit.git
    cd bioinformatics-toolkit
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    ```bash
    streamlit run app.py
    ```

4.  **Access:**
    Navigate to `http://localhost:8501` in your web browser.

---

## 🛠️ Technologies Used

*   **Python**: Core logic and data processing.
*   **Streamlit**: Frontend web framework for data applications.
*   **Biopython**: Robust library for biological computation and sequence analysis.

---

## 📝 Future Roadmap

*   [ ] Open Reading Frame (ORF) finder.
*   [ ] Support for FASTA and GenBank file uploads.
*   [ ] Restriction enzyme mapping.
*   [ ] Melting temperature ($T_m$) calculator.
*   [ ] Export results as PDF or CSV.

---

## 🤝 Contributing

Contributions are welcome! To contribute:
1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## 👤 Author

**Mehmet Erkan**

*   **GitHub**: [@mehmeterkann](https://github.com/mehmeterkann)
*   **LinkedIn**: [linkedin.com/in/mehmeterkann](https://www.linkedin.com/in/mehmet-e-erkan-45b841332/)

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---
