# CSCI 260: Master Study Guide & Table of Contents

## Introduction

This document serves as your comprehensive navigation tool for all study materials created for your CSCI 260 final exam. The exam will focus on processor architecture concepts, with 20% dedicated to the newer material including performance analysis, branch prediction, numeric representation, and microcoding.

## Table of Contents by Resource

### 1. Comprehensive Study Guide
- [MIPS Processor Architectures](#processor-architectures)
- [Performance Analysis](#performance-analysis)
- [Datapath and Control Design](#datapath-and-control)
- [Branch Prediction](#branch-prediction)
- [Numeric Representation](#numeric-representation)
- [Microcoding](#microcoding)
- [Pipeline Hazards and Solutions](#pipeline-hazards)
- [Custom Instruction Implementation](#custom-instructions)
- [Practice Problems](#practice-problems)
- [Key Formulas and References](#key-formulas)

### 2. In-Depth Processor Architecture Concepts
- [Understanding Processor Architectures: A Conceptual Journey](#processor-architectures-journey)
- [Performance Analysis: Beyond Basic Calculations](#performance-analysis-advanced)
- [Datapath and Control Implementation](#datapath-control-implementation)
- [Branch Prediction: Improving Pipeline Efficiency](#branch-prediction-efficiency)
- [Numeric Representation Systems](#numeric-representation-systems)
- [Microcoding: The Inner Control Layer](#microcoding-inner-layer)
- [Pipeline Hazards and Solutions](#pipeline-hazards-solutions)
- [Custom Instruction Implementation](#custom-instruction-implementation)
- [Understanding Pipelined MIPS: The Big Picture](#pipelined-mips-big-picture)
- [Final Exam Preparation Strategy](#exam-preparation-strategy)

### 3. MIPS Assembly Language Crash Course
- [MIPS Register File](#mips-register-file)
- [Instruction Formats](#instruction-formats)
- [Basic Instructions](#basic-instructions)
- [Addressing Modes](#addressing-modes)
- [Memory and Stack Operations](#memory-stack-operations)
- [Common Programming Patterns](#programming-patterns)
- [Important Concepts for Computer Architecture](#architecture-concepts)
- [Example: Connecting Assembly to Processor Implementation](#assembly-processor-connection)
- [Key Takeaways for the Exam](#assembly-takeaways)

### 4. Sample Exam with Solutions
- [Processor Architecture Concepts (True/False)](#concept-questions)
- [Critical Path Analysis](#critical-path-problem)
- [Performance Comparison](#performance-comparison)
- [Branch Prediction](#branch-prediction-problem)
- [Numeric Representation](#numeric-representation-problem)
- [Custom Instruction Implementation](#custom-instruction-problem)
- [Microcoding Implementation](#microcoding-problem)
- [Pipeline Hazards and Solutions](#pipeline-hazards-problem)
- [Optimizing Component Delays (Bonus)](#component-optimization)

## Detailed Topic Breakdown

<a id="processor-architectures"></a>
### MIPS Processor Architectures
- **Single-Cycle Architecture**
  - One instruction per clock cycle
  - Clock period determined by slowest instruction
  - CPI = 1
  - Simple control but inefficient timing
  - Resource utilization issues
  
- **Multi-Cycle Architecture**
  - Instructions divided into multiple steps
  - Different instructions take different number of cycles
  - Shorter clock period
  - Resource reuse between cycles
  - State machine control
  - Higher CPI but potentially better performance
  
- **Pipelined Architecture**
  - Five stages: IF, ID, EX, MEM, WB
  - Multiple instructions in different stages simultaneously
  - Pipeline registers between stages
  - Hazards reduce efficiency
  - Ideally approaches CPI of 1
  - Throughput vs. latency tradeoffs

<a id="performance-analysis"></a>
### Performance Analysis
- **Critical Path Analysis**
  - Definition and importance
  - Component delay identification
  - Path tracing methodology
  - Clock period calculation
  
- **Clock Rate Calculation**
  - Maximum frequency = 1 / Critical path delay
  - Impact of architecture on clock rate
  
- **CPI (Cycles Per Instruction)**
  - Single-cycle CPI = 1
  - Multi-cycle CPI calculation with instruction mix
  - Pipelined CPI with hazards
  - Effective CPI formula
  
- **MIPS Rating Calculation**
  - MIPS = (Clock rate) / (CPI × 10^6)
  - Limitations of MIPS as a metric
  
- **Component Timing**
  - MUX: 2 ps
  - Control Unit, ALU Control: 6 ps
  - ALU: 100 ps
  - Adder: 60 ps
  - Registers (PC, etc.): 3 ps read, 5 ps write
  - Memory: 70 ps read, 90 ps write
  - Register File: 30 ps read, 40 ps write

<a id="datapath-and-control"></a>
### Datapath and Control Design
- **Datapath Components**
  - Program Counter (PC)
  - Instruction Memory
  - Register File
  - ALU
  - Data Memory
  - Control Unit
  - Multiplexers
  
- **Control Signals**
  - RegDst, ALUSrc, MemtoReg, RegWrite
  - MemRead, MemWrite, Branch, Jump
  - ALUOp
  
- **Control Implementation**
  - Single-cycle: combinational logic
  - Multi-cycle: state machine
  - Control signal tables and timing

<a id="branch-prediction"></a>
### Branch Prediction
- **The Branch Problem**
  - Impact on pipeline efficiency
  - Branch frequency in typical programs
  
- **Branch Prediction Strategies**
  - Static prediction
  - 1-bit prediction
  - 2-bit saturating counter
  - Correlating predictors
  - Branch target buffer (BTB)
  
- **Performance Impact**
  - Misprediction penalty calculation
  - Effective CPI with branch prediction
  - Example calculations

<a id="numeric-representation"></a>
### Numeric Representation
- **IEEE 754 Floating Point**
  - Format breakdown (sign, exponent, fraction)
  - 32-bit single precision
  - Normalization process
  - Special values (±0, ±∞, NaN)
  - Conversion examples
  
- **Fixed Point Representation**
  - Format specification (integer.fraction)
  - Range and precision tradeoffs
  - Conversion process
  - Operations (addition, multiplication)

<a id="microcoding"></a>
### Microcoding
- **Control Implementation Options**
  - Hardwired vs. microcoded control
  - Tradeoffs between approaches
  
- **Microcode Architecture**
  - Control store
  - Microinstruction format
  - Microsequencer
  - Execution flow
  
- **Example Implementation**
  - jr instruction microcode
  - Timing analysis
  - Performance considerations
  
- **Pros and Cons**
  - Flexibility vs. performance
  - Complexity considerations
  - When to use microcoding

<a id="pipeline-hazards"></a>
### Pipeline Hazards and Solutions
- **Data Hazards**
  - Read-After-Write (RAW)
  - Write-After-Read (WAR)
  - Write-After-Write (WAW)
  - Examples and detection
  
- **Control Hazards**
  - Branch uncertainty
  - Branch prediction
  - Delayed branches
  - Performance impact
  
- **Structural Hazards**
  - Resource conflicts
  - Memory port limitations
  - Register file access
  
- **Hazard Solutions**
  - Forwarding (bypassing)
  - Stalling (pipeline bubbles)
  - Compiler techniques
  - Hardware vs. software approaches

<a id="custom-instructions"></a>
### Custom Instruction Implementation
- **Instruction Design Process**
  - Semantics definition
  - Machine code format
  - Datapath requirements
  - Control signals
  
- **Implementation Examples**
  - push/pop instructions
  - Store Twice (stw) instruction
  - Jump Direct Indirect (jdi) instruction
  - Swap Memory (swpm) instruction
  
- **Implementation Challenges**
  - Resource constraints
  - Timing considerations
  - Control complexity

<a id="practice-problems"></a>
### Practice Problems
- Critical path analysis examples
- Performance calculation problems
- Branch prediction exercises
- Number format conversion
- Custom instruction design
- Pipeline hazard analysis

<a id="key-formulas"></a>
### Key Formulas and References
- **Performance Formulas**
  - Execution Time = Instruction Count × CPI × Clock Cycle Time
  - CPI (Pipelined) = 1 + (Hazard stalls / Instruction count)
  - MIPS Rating = (Clock rate) / (CPI × 10^6)
  
- **MIPS Instruction Formats**
  - R-type: op (6), rs (5), rt (5), rd (5), shamt (5), funct (6)
  - I-type: op (6), rs (5), rt (5), immediate (16)
  - J-type: op (6), address (26)
  
- **Single-Cycle Control Signal Reference**
  - Control signal settings for basic instructions
  
- **Multi-Cycle State Machine Reference**
  - States and transitions
  - Control signals per state

## Last-Minute Study Plan

For the limited time remaining before your exam, focus on these high-priority areas:

1. **Performance Analysis (30 minutes)**
   - Review critical path analysis process
   - Practice one calculation for each architecture type
   - Memorize key formulas

2. **Architecture Comparisons (20 minutes)**
   - Strengths and weaknesses of each architecture
   - When each performs best
   - Key differences in implementation

3. **Branch Prediction and Hazards (20 minutes)**
   - Types of hazards and solutions
   - Branch prediction strategies
   - Performance impact calculations

4. **Newer Material Review (20 minutes)**
   - Numeric representation examples
   - Microcoding basics
   - Branch prediction performance

5. **Sample Problem Practice (30 minutes)**
   - Do at least one problem from each major section
   - Focus on understanding approach rather than completing all problems

Remember, understanding concepts is more important than memorizing specific implementations. Focus on grasping the fundamental principles and trade-offs in processor design.

## Quick Reference: Architecture Comparison

| Feature | Single-Cycle | Multi-Cycle | Pipelined |
|---------|-------------|------------|-----------|
| CPI | 1 | ~4-5 | ~1-1.2 |
| Clock Period | Longest path | Longest stage | Longest stage + overhead |
| Resource Usage | Low efficiency | High efficiency | High efficiency |
| Control Complexity | Simple | Medium | High |
| Hazards | None | None | Data, Control, Structural |
| Performance | Good for simple code | Good for memory-heavy code | Best for most code |
| Implementation Cost | Lowest | Medium | Highest |

## Quick Reference: Control Signals by Instruction Type

| Instruction | RegDst | ALUSrc | MemtoReg | RegWrite | MemRead | MemWrite | Branch | ALUOp | Jump |
|------------|--------|--------|----------|----------|---------|----------|--------|-------|------|
| R-type     | 1      | 0      | 0        | 1        | 0       | 0        | 0      | 10    | 0    |
| lw         | 0      | 1      | 1        | 1        | 1       | 0        | 0      | 00    | 0    |
| sw         | X      | 1      | X        | 0        | 0       | 1        | 0      | 00    | 0    |
| beq        | X      | 0      | X        | 0        | 0       | 0        | 1      | 01    | 0    |
| j          | X      | X      | X        | 0        | 0       | 0        | 0      | XX    | 1    |

## Exam Confidence Boosters

- The professor mentioned that understanding concepts is more important than memorizing diagrams
- You'll be given complex diagrams if needed during the exam
- Focus on understanding the "why" behind design decisions
- Your understanding of performance analysis and tradeoffs is most important
- Partial credit is likely available for showing your work and reasoning

Good luck on your exam tomorrow! With focused review of these materials, you're well-positioned to succeed.
