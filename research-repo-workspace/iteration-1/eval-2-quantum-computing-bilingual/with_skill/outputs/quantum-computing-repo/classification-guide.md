# Classification Guide

This document defines the tagging system for Quantum Computing research.

---

## Tag Categories

We use **4** tag categories with **14** total tags.

### Category 1: Data Type

**Purpose**: Characterizes the type of data or problem instances the quantum algorithm/method works with

**Tags:**
- **Benchmark**: Standardized datasets or problem instances for evaluation
- **Simulation**: Synthetic data from physics/chemistry simulations
- **Real_World**: Real-world application data (financial, chemical, industrial)

**Color scheme**: Blue gradient (dark → medium → light)

**Badge URLs:**
```
https://img.shields.io/badge/Benchmark-0052cc
https://img.shields.io/badge/Simulation-0066ff
https://img.shields.io/badge/Real_World-3399ff
```

**Examples:**
- "Quantum Machine Learning for Image Recognition" uses Real_World because it works with image datasets
- "VQE for Molecular Ground States" uses Simulation because it simulates molecular systems
- "Benchmarking Quantum Optimization Algorithms" uses Benchmark for standardized problem instances

---

### Category 2: Method

**Purpose**: Identifies the quantum algorithmic approach or technique

**Tags:**
- **VQA**: Variational Quantum Algorithms (VQE, QAOA, etc.)
- **Optimization**: Quantum optimization methods and algorithms
- **Machine_Learning**: Quantum machine learning approaches
- **Cryptography**: Quantum cryptography and post-quantum cryptography

**Color scheme**: Purple gradient (dark → medium → light)

**Badge URLs:**
```
https://img.shields.io/badge/VQA-6554c0
https://img.shields.io/badge/Optimization-8066ff
https://img.shields.io/badge/Machine_Learning-997dff
https://img.shields.io/badge/Cryptography-aa88ff
```

**Examples:**
- "Variational Quantum Eigensolver for Chemistry" uses VQA as it's a variational algorithm
- "Quantum Optimization for Logistics" uses Optimization for optimization methods
- "Quantum Neural Networks" uses Machine_Learning for ML approaches
- "Post-Quantum Cryptography Standards" uses Cryptography for cryptographic methods

---

### Category 3: Application

**Purpose**: Specifies the application domain or field

**Tags:**
- **Chemistry**: Quantum chemistry, molecular simulation, materials science
- **Finance**: Financial modeling, portfolio optimization, risk analysis
- **Optimization**: Combinatorial optimization, logistics, scheduling
- **Fundamental**: Fundamental quantum computing research without specific application

**Color scheme**: Green gradient (dark → medium → light)

**Badge URLs:**
```
https://img.shields.io/badge/Chemistry-008754
https://img.shields.io/badge/Finance-00a86b
https://img.shields.io/badge/Optimization-33d498
https://img.shields.io/badge/Fundamental-66e5b8
```

**Examples:**
- "Quantum Simulation of Molecular Systems" uses Chemistry for chemistry applications
- "Quantum Portfolio Optimization" uses Finance for financial applications
- "Quantum Algorithm for Vehicle Routing" uses Optimization for optimization problems
- "Quantum Algorithm for Linear Systems" uses Fundamental as it's a fundamental algorithm

---

### Category 4: Special Properties

**Purpose**: Identifies special characteristics or requirements

**Tags:**
- **Error_Correction**: Focuses on quantum error correction techniques
- **Fault_Tolerant**: Requires or assumes fault-tolerant quantum computation
- **NISQ**: Designed for Noisy Intermediate-Scale Quantum (NISQ) devices
- **Hybrid**: Quantum-classical hybrid approaches

**Color scheme**: Orange gradient (dark → medium → light)

**Badge URLs:**
```
https://img.shields.io/badge/Error_Correction-ff6b00
https://img.shields.io/badge/Fault_Tolerant-ff8c00
https://img.shields.io/badge/NISQ-ffab33
https://img.shields.io/badge/Hybrid-ffcc66
```

**Examples:**
- "Surface Code Implementation for Quantum Error Correction" uses Error_Correction
- "Fault-Tolerant Quantum Fourier Transform" uses Fault_Tolerant
- "Variational Algorithms for NISQ Devices" uses NISQ
- "Hybrid Quantum-Classical Optimization" uses Hybrid

---

## Tag Selection Rules

**Required:**
- 1 primary tag from **Application** category

**Optional:**
- 1 tag from **Method** category
- 1 tag from **Data Type** category
- 1 tag from **Special Properties** category

**Total: 2-4 tags per paper**

---

## Selection Decision Tree

```
Start: What is the primary application domain?
├─ Chemistry/Simulation → Tag: Chemistry
├─ Finance/Economics → Tag: Finance
├─ Optimization/Logistics → Tag: Optimization
└─ Fundamental/General → Tag: Fundamental

Secondary: What is the main method?
├─ Variational approach → Tag: VQA
├─ Optimization technique → Tag: Optimization
├─ Machine learning → Tag: Machine_Learning
└─ Cryptography → Tag: Cryptography

Tertiary: What data type?
├─ Standard benchmarks → Tag: Benchmark
├─ Simulated data → Tag: Simulation
└─ Real-world data → Tag: Real_World

Quaternary: Special properties?
├─ Error correction focus → Tag: Error_Correction
├─ Fault-tolerant required → Tag: Fault_Tolerant
├─ NISQ device → Tag: NISQ
└─ Hybrid approach → Tag: Hybrid
```

---

## Color Best Practices

1. **Use gradients within categories**: Dark → medium → light
2. **Maintain contrast**: Ensure WCAG AA compliance (4.5:1 ratio)
3. **Distinguish categories**: Use different base colors (blue, green, purple, orange)

**Recommended color values:**
- Blue: `0052cc`, `0066ff`, `3399ff`
- Green: `008754`, `00a86b`, `33d498`
- Purple: `6554c0`, `8066ff`, `997dff`
- Orange: `ff6b00`, `ff8c00`, `ffab33`

---

## Common Mistakes

- **Don't**: Use more than 4 tags (too many dilutes meaning)
- **Do**: Focus on 2-3 most relevant tags

- **Don't**: Mix tags from same category (e.g., 2 method tags)
- **Do**: Choose one representative tag per category max

- **Don't**: Use tags without understanding their definition
- **Do**: Refer to this guide when unsure

---

## Example Tag Combinations

**Example 1**: "Variational Quantum Eigensolver for Molecular Ground States"
- Chemistry (Application)
- VQA (Method)
- Simulation (Data Type)
- NISQ (Special Properties)

**Example 2**: "Quantum Optimization for Portfolio Management"
- Finance (Application)
- Optimization (Method)
- Real_World (Data Type)
- Hybrid (Special Properties)

**Example 3**: "Fault-Tolerant Quantum Algorithm for Linear Systems"
- Fundamental (Application)
- Fault_Tolerant (Special Properties)
- Benchmark (Data Type)

---
