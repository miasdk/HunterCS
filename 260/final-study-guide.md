# CSCI 260: Comprehensive Final Exam Study Guide

## Table of Contents
1. [MIPS Processor Architectures](#mips-processor-architectures)
2. [Performance Analysis](#performance-analysis)
3. [Datapath and Control Design](#datapath-and-control-design)
4. [Branch Prediction](#branch-prediction)
5. [Numeric Representation](#numeric-representation)
6. [Microcoding](#microcoding)
7. [Pipeline Hazards and Solutions](#pipeline-hazards-and-solutions)
8. [Custom Instruction Implementation](#custom-instruction-implementation)
9. [Practice Problems](#practice-problems)
10. [Key Formulas and References](#key-formulas-and-references)

---

## MIPS Processor Architectures

### 1. Single-Cycle Architecture

**Key Concepts:**
- Each instruction completes in one clock cycle
- Clock cycle time determined by the slowest instruction
- Simple control but inefficient timing

**Characteristics:**
- No resource reuse within an instruction
- Separate instruction and data memories
- CPI (Cycles Per Instruction) = 1
- Long clock period due to critical path
- Wastes resources since not all instructions use all components

**Datapath Elements:**
- PC (Program Counter)
- Instruction Memory
- Register File
- ALU (Arithmetic Logic Unit)
- Data Memory
- Control Unit
- Various multiplexers for routing

### 2. Multi-Cycle Architecture

**Key Concepts:**
- Instructions broken into multiple steps/cycles
- Each step takes one clock cycle
- Different instructions may take different numbers of cycles
- Resources reused across cycles

**Cycle Breakdown:**
1. Fetch instruction
2. Decode and register fetch
3. Execute operation or calculate address
4. Memory access (if needed)
5. Write back (if needed)

**Advantages:**
- Shorter clock period
- Better resource utilization
- Improved performance for many instructions

**Control Implementation:**
- State machine approach
- Each state defines control signals
- Transitions based on instruction type

### 3. Pipelined Architecture

**Key Concepts:**
- Multiple instructions in different stages of execution simultaneously
- Five stages: Fetch (IF), Decode (ID), Execute (EX), Memory (MEM), Write-back (WB)
- Ideally, CPI approaches 1 with full pipeline

**Performance Factors:**
- Pipeline hazards reduce efficiency (data, control, structural)
- Forwarding and stalling mechanisms required
- Branch prediction critical for performance

**Throughput vs. Latency:**
- Throughput: Instructions completed per unit time
- Latency: Time to complete a single instruction
- Pipelining improves throughput but not latency

---

## Performance Analysis

### Timing Components
- **MUX**: 2 ps
- **Control Unit, ALU Control**: 6 ps
- **ALU**: 100 ps
- **Adder**: 60 ps
- **Registers (PC, IR, MDR, A, B, ALUOut, Pipelines)**: 3 ps read, 5 ps write
- **Memory (data, instruction)**: 70 ps read, 90 ps write
- **Register File**: 30 ps read, 40 ps write

### Critical Path Analysis

**Single-Cycle:**
- Critical path includes all components in the longest instruction execution path
- Clock period must accommodate worst-case path
- Example path: PC → Instruction Memory → Register File → ALU → Data Memory → Register File

**Multi-Cycle:**
- Each cycle has its own critical path
- Clock period determined by the longest cycle's path
- Example paths:
  - Fetch: PC → Instruction Memory → IR
  - Execute: A/B → ALU → ALUOut

**Pipelined:**
- Each stage has its own critical path
- Clock period determined by the slowest stage
- Hazards may introduce additional delays

### Performance Metrics

**Clock Rate Calculation:**
- Clock rate = 1 / (Critical path delay)

**MIPS Rating Calculation:**
- MIPS = (Instruction count × Clock rate) / (CPI × 10^6)
- For single-cycle: CPI = 1
- For multi-cycle: CPI = average cycles per instruction type
- For pipelined: CPI = 1 + (hazard stalls / instruction count)

**Instruction Mix Impact:**
- R-type: 64%
- Branch: 15%
- Load: 10%
- Store: 6%
- Jump: 5%

**Example Calculation:**
For single-cycle architecture:
1. Identify critical path delay (e.g., PC → IM → RF → ALU → DM → RF)
2. Calculate clock period from components (e.g., 3 + 70 + 30 + 100 + 70 + 40 = 313 ps)
3. Calculate clock rate (1/313 ps = 3.2 GHz)
4. Calculate MIPS rating considering instruction mix

---

## Datapath and Control Design

### Single-Cycle Datapath
- **Control signals**: ALUSrc, RegDst, RegWrite, MemRead, MemWrite, MemtoReg, Branch, Jump
- **ALU operations**: ADD, SUB, AND, OR, SLT, etc.
- **Data routing**: Multiplexers direct data flow based on instruction type

### Multi-Cycle Datapath
- **Additional registers**: IR (Instruction Register), MDR (Memory Data Register), A, B, ALUOut
- **Control signals**: IorD, IRWrite, PCWrite, PCWriteCond, ALUSrcA, ALUSrcB, ALUOp, etc.
- **State machine controller**: Controls processor states and transitions

### Control Tables

**Single-Cycle Control:**

| Instr | RegDst | ALUSrc | MemToReg | RegWrite | MemRead | MemWrite | Branch | ALUOp | Jump |
|-------|--------|--------|----------|----------|---------|----------|--------|-------|------|
| R-type| 1      | 0      | 0        | 1        | 0       | 0        | 0      | OP    | 0    |
| lw    | 0      | 1      | 1        | 1        | 1       | 0        | 0      | ADD   | 0    |
| sw    | X      | 1      | X        | 0        | 0       | 1        | 0      | ADD   | 0    |
| beq   | X      | 0      | X        | 0        | 0       | 0        | 1      | SUB   | 0    |
| j     | X      | X      | X        | 0        | 0       | 0        | X      | X     | 1    |

**Multi-Cycle State Machine:**
- Each state defines a set of control signals
- Transitions depend on instruction type
- States include: Fetch, Decode, Execute, Memory Access, Write-back

---

## Branch Prediction

### Branch Prediction Strategies
- **Static prediction**: Always predict taken/not-taken
- **1-bit prediction**: Remember last outcome
- **2-bit prediction**: Counters with hysteresis (strongly taken, weakly taken, etc.)
- **Branch target buffer (BTB)**: Cache of branch targets

### Performance Impact
- Misprediction penalty = number of pipeline stages that need to be flushed
- Branch frequency in code affects overall impact
- Formula: Average CPI = base CPI + (branch frequency × misprediction rate × penalty)

### Example Problem
Calculate throughput with:
- Mispredictions requiring 4 cycle stall
- Branch prediction accuracy of 95%
- 1/7 of instructions are branches
- Pipeline running at 2 GHz
- All data hazards handled by forwarding

**Approach:**
1. Calculate branch misprediction rate: 5% (100% - 95%)
2. Calculate frequency of mispredictions: 1/7 × 0.05 = 0.00714
3. Calculate average CPI: 1 + (0.00714 × 4) = 1.0286
4. Calculate throughput: (2 × 10^9) / 1.0286 = 1.94 BIPS (billion instructions per second)

---

## Numeric Representation

### Floating Point (IEEE 754)
- **32-bit format**: 1 bit sign, 8 bits exponent, 23 bits fraction
- **Bias**: 127 for single precision
- **Special values**: ±0, ±∞, NaN

**Conversion Process:**
1. Normalize number to 1.xxx × 2^y format
2. Add bias to exponent
3. Store fraction (mantissa) without leading 1

**Example**: Representing 0.15625
- Binary: 0.00101
- Normalized: 1.01 × 2^(-3)
- Exponent: -3 + 127 = 124 = 01111100
- Sign bit: 0
- Fraction: 01000...0
- Final: 0 01111100 01000...0

### Fixed Point
- **Format**: Divide bits between integer and fractional parts
- **Range vs. precision tradeoff**: More integer bits increase range; more fraction bits increase precision

**Conversion Process:**
1. Determine bit allocation (e.g., 16.16 format: 16 bits integer, 16 bits fraction)
2. Convert integer part to binary
3. Convert fractional part to binary (multiply by 2 method)
4. Combine parts

---

## Microcoding

### Microcode Concepts
- **Microinstruction**: Low-level control signals that implement machine instructions
- **Microprogram**: Sequence of microinstructions
- **Control store**: Memory that holds microcode
- **Microsequencer**: Controls flow through microprogram

### Microcode Implementation
- **Horizontal microcode**: Wide format, many control signals directly encoded
- **Vertical microcode**: Narrow format, uses encoding to reduce width

### Implementation Example (jr instruction)
- **RTL (Register Transfer Logic)**: PC ← R[rs]
- **Microoperations**:
  1. Read register rs
  2. Transfer value to PC

### Performance Considerations
- **Microcode Storage**: 25 ps
- **Adder**: 15 ps
- **Critical path**: Includes microcode fetch and execution

### Pros and Cons
- **Pros**:
  - Flexible and easily modified
  - Simplifies hardware design
  - Facilitates complex instructions
- **Cons**:
  - Slower than hardwired control
  - Requires additional memory
  - Adds complexity to timing analysis

---

## Pipeline Hazards and Solutions

### 1. Data Hazards
- **Read-after-write (RAW)**: Instruction needs result from previous instruction
- **Write-after-read (WAR)**: Instruction overwrites data needed by previous instruction
- **Write-after-write (WAW)**: Multiple instructions write to same register

**Solutions**:
- **Forwarding (bypassing)**: Route results directly to where needed
- **Stalling (pipeline bubbles)**: Delay execution until data available
- **Compiler scheduling**: Rearrange code to avoid hazards

### 2. Control Hazards
- **Branch uncertainty**: Next instruction depends on branch outcome
- **Jump targets**: Changing program counter disrupts sequential flow

**Solutions**:
- **Branch prediction**: Guess branch direction
- **Delayed branches**: Execute instruction after branch regardless
- **Branch target buffer**: Cache branch destinations

### 3. Structural Hazards
- **Resource conflicts**: Multiple instructions need same hardware component

**Solutions**:
- **Resource duplication**: Add more hardware (e.g., separate instruction/data caches)
- **Pipelining components**: Allow multiple accesses at different stages
- **Stalling**: Delay instruction until resource available

---

## Custom Instruction Implementation

### Implementation Process
1. **Define instruction semantics**: What does the instruction do?
2. **Determine machine code format**: How is it encoded?
3. **Identify datapath elements**: What components are needed?
4. **Modify control signals**: Add/change signals for new behavior
5. **Update control tables/state machines**: Include new instruction

### Example Instructions

**1. Push Register (push reg)**
- **Semantics**: Decrement stack pointer, store register at new location
- **Machine code format**: Use immediate field for specific encoding (e.g., 410)
- **Implementation**:
  - Add control signals for decrementing SP
  - Sequence memory write after SP update

**2. Store Twice (stw regx,offset(regy))**
- **Semantics**: Store regx to offset(regy) and offset+4(regy), then add 4 to regy
- **Machine code format**: Similar to standard store
- **Implementation**:
  - Reuse ALU for address calculation twice
  - Add control signals for second store
  - Add SP increment operation

**3. Jump Direct Indirect (jdi regx,regy)**
- **Semantics**: If regx > 0, jump to address in regx; else jump to address in mem[regy]
- **Machine code format**: R-type format
- **Implementation**:
  - Add conditional logic for jump target selection
  - Modify PC source multiplexer

---

## Practice Problems

### Problem 1: Critical Path Analysis
Identify the critical path for a MIPS single-cycle architecture executing an R-type instruction. Calculate the maximum clock frequency given the component delays.

**Solution approach**:
1. Trace instruction execution from fetch to write-back
2. Add up delays of components in the path
3. Calculate clock frequency as 1/total delay

### Problem 2: Multi-cycle MIPS Control
Design control signals for implementing the `jr` instruction on multi-cycle MIPS.

**Solution approach**:
1. Break instruction into steps (fetch, decode, execute)
2. Identify required datapath connections
3. Define control signals for each step
4. Add states to state machine diagram

### Problem 3: Pipelined Performance
Calculate the effective MIPS rating for a pipelined processor with branch prediction accuracy of 90%, branch frequency of 20%, and a 3-cycle misprediction penalty.

**Solution approach**:
1. Calculate average CPI with stalls
2. Determine throughput based on clock rate
3. Convert to MIPS rating

---

## Key Formulas and References

### Performance Formulas
- **Clock Rate**: 1 / Critical Path Delay
- **CPI (Single-cycle)**: 1
- **CPI (Multi-cycle)**: Weighted average of cycles per instruction type
- **CPI (Pipeline)**: 1 + (Hazard stalls / Instruction count)
- **MIPS Rating**: (Instruction count × Clock rate) / (CPI × 10^6)
- **Execution Time**: Instruction count × CPI × Clock cycle time

### MIPS Instruction Formats
- **R-type**: op (6 bits), rs (5), rt (5), rd (5), shamt (5), funct (6)
- **I-type**: op (6 bits), rs (5), rt (5), immediate (16)
- **J-type**: op (6 bits), address (26)

### Control Signal Reference

**Single-Cycle Control Signals**:
- RegDst: Selects destination register
- ALUSrc: Selects second ALU input
- MemtoReg: Selects data for register write
- RegWrite: Enables register writing
- MemRead: Enables memory reading
- MemWrite: Enables memory writing
- Branch: Enables branch logic
- ALUOp: Selects ALU operation
- Jump: Enables jump operation

**Multi-Cycle Additional Control Signals**:
- IorD: Selects memory address source
- IRWrite: Enables instruction register writing
- PCWrite: Enables PC writing
- PCWriteCond: Conditionally enables PC writing
- ALUSrcA: Selects first ALU input
- ALUSrcB: Selects second ALU input
- PCSource: Selects next PC value

### Study Tips
1. **Focus on concepts**: Understand why architectures are designed certain ways
2. **Practice calculations**: Work through performance analysis problems
3. **Compare architectures**: Know trade-offs between single-cycle, multi-cycle, and pipelined designs
4. **Understand data flow**: Trace instruction execution through datapaths
5. **Know performance bottlenecks**: Identify critical paths and hazards

### Exam Preparation Checklist
- [ ] Understand single-cycle MIPS datapath and control
- [ ] Understand multi-cycle MIPS datapath and control
- [ ] Understand pipelined MIPS and hazard solutions
- [ ] Practice critical path analysis
- [ ] Practice performance calculations
- [ ] Understand branch prediction strategies
- [ ] Know how to implement custom instructions
- [ ] Understand floating point and fixed point representation
- [ ] Know pros and cons of microcoded implementations
- [ ] Practice tracing instruction execution through different architectures
