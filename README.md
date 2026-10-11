# Project Levante

Project Levante is an edge-AI system for providing early, continuous estimates of bacterial risk in bathing water along the Mediterranean coast.

## Repository layout

| Path | Contents |
| --- | --- |
| `main.c` | STM32 firmware that samples the analogue turbidity sensor and sends raw readings over UART. |
| `Experiments/` | Recorded sensor data and scripts for the exploratory regression analysis. |
| `Library/` | Exported NanoEdge AI classifier library and its metadata. |
| `Report.pdf` | Project report. |

The firmware currently reports raw ADC values. Conversion to calibrated turbidity units is a future calibration task.

## The problem

Current laboratory culture testing detects bacterial contamination, but results take 24–48 hours. By then, swimmers may already have entered the water. This creates a public-health risk and can disrupt the coastal tourism economy.

Levante treats this as a latency problem: reduce the time from a contamination event to an actionable decision.

## The solution

A solar-powered buoy continuously measures environmental indicators, including turbidity, rainfall, temperature, and conductivity. An on-board model turns these readings into a real-time risk score.

When the score rises, Levante alerts an accredited field team to collect a targeted sample. A portable qPCR device then confirms the result in roughly three hours.

The system follows a clear principle: **prediction directs; measurement decides.** The model does not close beaches—it prioritizes where to sample. Closure decisions remain with the accredited laboratory and public authority.

## Customer and circular model

The intended customer is the accredited testing laboratory. Accredited results are legally admissible, while laboratories are not typically equipped to operate marine sensing infrastructure at scale.

Buoys are leased rather than sold. At end of life, each unit is returned for reuse, repair, or recycling.

## Prototype and next steps

During a two-week programme, the team delivered a working turbidity sensing-and-classification node based on an STM32 microcontroller and an on-device anomaly-detection model. The prototype validated optical separation between clear and turbid water.

The original objective was also to perform a regression analysis that would convert the optical sensor readings into actual turbidity values. Hardware difficulties prevented the collection of the calibrated reference measurements needed to establish and validate that conversion. The available experiment data therefore support relative comparisons between water conditions, rather than a calibrated turbidity measurement.

The proposed workflow is projected to roughly halve the time between a contamination event and an actionable decision. Remaining work includes building the full buoy and training the predictive model with field data.

## Team

| Member | Principal contribution |
| --- | --- |
| Riccardo Cirillo | Entrepreneurship, economics, communication, business and circular canvases, and pitch |
| Victor G. De Matteis | Autonomous systems, entrepreneurship, research, documentation, and overall project direction |
| Raul Frandes | Computer science, AI, machine learning, and embedded-systems programming |
| Carolina Mata | Technical work, especially electronic-circuit design and implementation |
| Giorgio Perakis | Mechanical design, critical sense-making, and embedded-systems programming |
| Peng Ying | Graphics, information design, and professional-document production |

More details are available in `Report.pdf`.
