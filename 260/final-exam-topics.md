# Computer Architecture Final Exam - Comprehensive Answers

## Table of Contents

1. [Processor Architectures Overview](#1-processor-architectures-overview)
   - [1.1 Single-Cycle MIPS Architecture](#11-single-cycle-mips-architecture)
   - [1.2 Multi-Cycle MIPS Architecture](#12-multi-cycle-mips-architecture)
   - [1.3 Pipelined MIPS Architecture](#13-pipelined-mips-architecture)
   - [1.4 Microcoded Architecture](#14-microcoded-architecture)
   - [1.5 Comparing Architectures: When to Use Each](#15-comparing-architectures-when-to-use-each)

2. [Performance Analysis](#2-performance-analysis)
   - [2.1 Throughput vs. Latency](#21-throughput-vs-latency)
   - [2.2 Performance Calculation](#22-performance-calculation)
   - [2.3 Cycle Count Analysis](#23-cycle-count-analysis)

3. [Pipeline Concepts and Hazards](#3-pipelining-concepts-and-hazards)
   - [3.1 Pipeline Fundamentals](#31-pipeline-fundamentals)
   - [3.2 Pipeline Hazards](#32-pipeline-hazards)
   - [3.3 Forwarding Mechanism](#33-forwarding-mechanism)
   - [3.4 Stalling Mechanism](#34-stalling-mechanism)

4. [Branch Prediction](#4-branch-prediction)
   - [4.1 Branch Prediction Fundamentals](#41-branch-prediction-fundamentals)
   - [4.2 2-Bit Saturating Counter Predictor](#42-2-bit-saturating-counter-predictor)
   - [4.3 Advanced Branch Prediction](#43-advanced-branch-prediction)
   - [4.4 Impact on Performance](#44-impact-on-performance)

5. [Assembly Implementation of Stack Operations](#5-assembly-implementation-of-stack-operations)
   - [5.1 Stack Concept in MIPS](#51-stack-concept-in-mips)
   - [5.2 Implementing Push Operation](#52-implementing-push-operation)
   - [5.3 Implementing Pop Operation](#53-implementing-pop-operation)

6. [Custom Instruction Design](#6-custom-instruction-design)
   - [6.1 General Process for Adding Instructions](#61-general-process-for-adding-instructions)
   - [6.2 Example: Implementing a Custom Instruction](#62-example-implementing-a-custom-instruction)
   - [6.3 Challenges in Custom Instruction Design](#63-challenges-in-custom-instruction-design)

7. [Branch Prediction](#7-branch-prediction)
   - [7.1 Branch Prediction Fundamentals](#71-branch-prediction-fundamentals)
   - [7.2 2-Bit Saturating Counter Predictor](#72-2-bit-saturating-counter-predictor)
   - [7.3 Advanced Branch Prediction](#73-advanced-branch-prediction)
   - [7.4 Impact on Performance](#74-impact-on-performance)

8. [Summary of Key Takeaways](#summary-of-key-takeaways)

## 1. Processor Architectures Overview

### 1.1 Single-Cycle MIPS Architecture

#### Core Concepts
In a single-cycle MIPS architecture, every instruction executes in exactly one clock cycle. This means the entire instruction process—fetch, decode, execute, memory access, and write-back—must complete within a single clock period.

#### Datapath Components
- **PC (Program Counter)**: Holds the address of the current instruction
- **Instruction Memory**: Stores the program instructions
- **Register File**: Provides fast access to register values
- **ALU (Arithmetic Logic Unit)**: Performs computations
- **Data Memory**: Stores data that doesn't fit in registers
- **Control Unit**: Generates signals to control datapath components

#### Why Use Single-Cycle?
**Advantages:**
- Conceptual simplicity: Straightforward implementation and debugging
- No resource conflicts: Each component used once per instruction
- No control complexity: No need for pipeline registers or hazard handling

**Disadvantages:**
- Clock period determined by the slowest instruction (usually load word)
- Inefficient resource utilization: Many components idle during each cycle
- Poor performance for complex programs

#### What Makes Single-Cycle Slow?
Programs with many memory operations (loads/stores) are particularly inefficient on single-cycle architectures. Since the clock cycle must accommodate the entire load word path (PC → Instruction Memory → Register File → ALU → Data Memory → Register File), even simple instructions waste time waiting for this long clock period to complete.

### 1.2 Multi-Cycle MIPS Architecture

#### Core Concepts
The multi-cycle architecture breaks each instruction into multiple steps, with each step taking one clock cycle. Different instruction types can use different numbers of cycles based on their complexity.

#### Typical Cycles per Instruction
- R-type instructions: 4 cycles
- Load instructions: 5 cycles
- Store instructions: 4 cycles
- Branch instructions: 3 cycles
- Jump instructions: 3 cycles

#### Datapath Enhancements
Multi-cycle adds several registers to the datapath:
- **Instruction Register (IR)**: Holds the current instruction
- **Memory Data Register (MDR)**: Holds data read from memory
- **A and B Registers**: Hold values read from the register file
- **ALUOut Register**: Holds the ALU result

#### Control Implementation
Multi-cycle control is implemented as a finite state machine (FSM), with states for:
1. Fetch instruction
2. Decode instruction/read registers
3. Execute operation or calculate address
4. Access memory (if needed)
5. Write back result (if needed)

#### Why Use Multi-Cycle?
**Advantages:**
- Shorter clock period: Determined by the longest individual stage
- Better resource utilization: Components reused across cycles
- Flexibility in CPI: Different instructions take appropriate number of cycles

**Disadvantages:**
- More complex control (state machine)
- Higher overall CPI than pipelined
- Sequential execution (one instruction at a time)

### 1.3 Pipelined MIPS Architecture

#### Core Concepts
Pipelining divides instruction execution into fixed stages and allows multiple instructions to execute simultaneously in different stages. The classic MIPS pipeline has five stages:
1. **IF (Instruction Fetch)**: Fetch instruction from memory
2. **ID (Instruction Decode)**: Decode instruction and read registers
3. **EX (Execute)**: Perform ALU operation or address calculation
4. **MEM (Memory Access)**: Access memory if needed
5. **WB (Write Back)**: Write result to register file

#### Pipeline Registers
Pipeline registers store intermediate results between stages:
- **IF/ID**: Holds the fetched instruction
- **ID/EX**: Holds decoded information and register values
- **EX/MEM**: Holds ALU result and control signals for memory
- **MEM/WB**: Holds data read from memory and control for write-back

#### Performance Metrics
- **Ideal CPI**: 1 (one instruction completed per cycle once pipeline is full)
- **Throughput**: Instructions per second (approaches clock rate in ideal case)
- **Latency**: Time to complete a single instruction (5 cycles in 5-stage pipeline)

#### Why Use Pipelining?
**Advantages:**
- Significantly higher throughput than single-cycle or multi-cycle
- Better resource utilization
- Scalable performance with instruction-level parallelism

**Disadvantages:**
- Increased complexity (pipeline registers, hazard detection/handling)
- Hazards can reduce performance
- Higher hardware cost and power consumption

### 1.4 Microcoded Architecture

#### Core Concepts
Microcoding implements complex instructions using simpler microinstructions stored in a control store (microprogram memory). Each machine instruction corresponds to a sequence of microinstructions.

#### Key Components
- **Control Store**: ROM/RAM holding microinstructions
- **Microinstruction Register**: Holds current microinstruction
- **Microsequencer**: Controls flow through microprogram
- **Microinstruction Decoder**: Generates actual control signals

#### Microinstruction Format Options
- **Horizontal**: Wide format with direct control signals (less encoding, faster)
- **Vertical**: Narrow format with encoded fields (more compact, slower)

#### Why Use Microcoding?
**Advantages:**
- Supports complex instruction sets
- Easier to debug and modify
- Simplifies implementation of complex operations
- Better code density with powerful instructions

**Disadvantages:**
- Slower execution than hardwired control
- Higher memory requirements for control store
- Complex to optimize

### 1.5 Comparing Architectures: When to Use Each

#### Single-Cycle
**Best for:**
- Educational purposes
- Very simple processors
- Applications where consistency is more important than speed

#### Multi-Cycle
**Best for:**
- Simple microcontrollers
- Systems with varied instruction costs
- Applications with tight power constraints

#### Pipelined
**Best for:**
- General-purpose computing
- Applications requiring high throughput
- Modern processors across the performance spectrum

#### Microcoded
**Best for:**
- Complex instruction sets (CISC)
- Systems needing instruction flexibility
- Legacy support in modern processors

## 2. Performance Analysis

### 2.1 Throughput vs. Latency

#### Throughput
**Definition**: The rate at which instructions are completed (instructions per second).

**Formula**: Throughput = Clock Rate / CPI

**In different architectures:**
- **Single-cycle**: Throughput = Clock Rate (but Clock Rate is low due to long cycle time)
- **Multi-cycle**: Throughput = Clock Rate / Average CPI (better Clock Rate, but higher CPI)
- **Pipelined**: Throughput approaches Clock Rate in ideal case (high Clock Rate, CPI approaches 1)

#### Latency
**Definition**: The time taken to complete a single instruction from start to finish.

**Formula**: Latency = CPI × Clock Period

**In different architectures:**
- **Single-cycle**: Latency = Clock Period (high due to long clock period)
- **Multi-cycle**: Latency = Number of Cycles × Clock Period (varies by instruction)
- **Pipelined**: Latency = Number of Stages × Clock Period (fixed at 5 cycles for 5-stage pipeline)

#### Which Architecture Optimizes Which Metric?
- **Single-cycle**: Optimizes latency for simple instructions (one cycle, but long cycle time)
- **Multi-cycle**: Balances throughput and latency (shorter cycle time but multiple cycles)
- **Pipelined**: Optimizes throughput at the expense of latency (high throughput, fixed latency)

### 2.2 Performance Calculation

#### Key Performance Metrics
- **Execution Time**: The total time to run a program
- **MIPS (Million Instructions Per Second)**: Rate of instruction execution
- **CPI (Cycles Per Instruction)**: Average cycles needed per instruction

#### Fundamental Performance Equation
Execution Time = Instruction Count × CPI × Clock Cycle Time

#### Example Calculation
For a program with 1 million instructions on a processor with average CPI of 2.5 and clock rate of 2 GHz:
- Clock Cycle Time = 1/2 GHz = 0.5 ns
- Execution Time = 1,000,000 × 2.5 × 0.5 ns = 1.25 ms
- MIPS = (1,000,000 instructions) / (1.25 ms) = 800 MIPS

#### Performance with Pipelining and Hazards
For a pipelined processor with base CPI of 1, branch frequency of 20%, and branch misprediction rate of 10% with 3-cycle penalty:
- Average CPI = 1 + (0.20 × 0.10 × 3) = 1 + 0.06 = 1.06
- This represents a 6% performance reduction due to branch mispredictions

### 2.3 Cycle Count Analysis

#### Calculating Cycles for a Program
1. Identify the instruction mix (percentages of each instruction type)
2. Determine cycles per instruction for each type
3. Calculate weighted average CPI
4. Multiply by instruction count to get total cycles

#### Example for Multi-Cycle MIPS
For a program with:
- 60% R-type (4 cycles each)
- 20% Loads (5 cycles each)
- 15% Stores (4 cycles each)
- 5% Branches (3 cycles each)

Average CPI = (0.60 × 4) + (0.20 × 5) + (0.15 × 4) + (0.05 × 3) = 4.15

For a 1 million instruction program:
Total cycles = 1,000,000 × 4.15 = 4,150,000 cycles

#### Example for Pipelined MIPS
For an ideal pipeline with no hazards:
- First instruction: 5 cycles
- Each subsequent instruction: 1 additional cycle

For a program with 1 million instructions:
Total cycles = 5 + (1,000,000 - 1) = 1,000,004 cycles

With hazards (assuming effective CPI of 1.2):
Total cycles = 5 + (1,000,000 - 1) × 1.2 = 1,200,004 cycles

## 3. Pipelining Concepts and Hazards

### 3.1 Pipeline Fundamentals

#### Pipeline Stages (5-stage MIPS)
1. **IF (Instruction Fetch)**:
   - PC → Instruction Memory → IF/ID Register
   - PC updated to PC+4

2. **ID (Instruction Decode)**:
   - Instruction decoded
   - Register File read
   - Control signals generated
   - Branch target calculated

3. **EX (Execute)**:
   - ALU operation performed
   - Branch condition evaluated
   - Jump/branch target finalized

4. **MEM (Memory Access)**:
   - Data memory read/write if needed
   - PC updated for taken branches

5. **WB (Write Back)**:
   - Results written to Register File

#### Pipeline Diagram
```
Time →
IF  | ID  | EX  | MEM | WB  |     Instruction 1
    | IF  | ID  | EX  | MEM | WB  Instruction 2
        | IF  | ID  | EX  | MEM | WB  Instruction 3
            | IF  | ID  | EX  | MEM | WB  Instruction 4
                | IF  | ID  | EX  | MEM | WB  Instruction 5
```

#### Pipeline Speedup
**Ideal Speedup** = Number of Pipeline Stages

For a 5-stage pipeline:
- Ideal CPI = 1 (vs. ~4-5 for multi-cycle)
- Theoretical speedup = 5× (vs. single-cycle with equivalent stage delays)
- Actual speedup < 5× due to pipeline registers overhead and hazards

### 3.2 Pipeline Hazards

#### A. Data Hazards

Data hazards occur when an instruction depends on the result of a previous instruction still in the pipeline.

**Types of Data Hazards:**

1. **RAW (Read After Write)**: Most common - instruction tries to read operand before previous instruction writes it.
   ```
   add $t0, $t1, $t2    # Write to $t0
   sub $t3, $t0, $t4    # Read from $t0 before it's ready
   ```

2. **WAR (Write After Read)**: Less common in MIPS - instruction tries to write operand before previous instruction reads it.
   ```
   add $t0, $t1, $t2    # Read from $t1
   sub $t1, $t3, $t4    # Write to $t1 before it's read
   ```

3. **WAW (Write After Write)**: Less common in MIPS - instruction tries to write operand before previous instruction writes it.
   ```
   add $t0, $t1, $t2    # Write to $t0
   sub $t0, $t3, $t4    # Write to $t0 again before first write completes
   ```

**MIPS Handling of Data Hazards:**
- **Forwarding** (Bypassing): Hardware detects when a register value is needed before it's written back and routes it directly from the pipeline register
- **Stalling**: When forwarding isn't possible, pipeline is stalled by inserting "bubbles"
- **Compiler Scheduling**: Reorganizing code to minimize hazards

#### B. Control Hazards

Control hazards occur when the flow of instruction execution depends on a branch or jump instruction.

**Branch Handling Methods:**
1. **Stall**: Wait until branch decision is made (3-cycle penalty in 5-stage pipeline)
2. **Predict-not-taken**: Continue fetching sequentially; flush if branch taken
3. **Predict-taken**: Fetch from branch target; flush if not taken
4. **Dynamic Prediction**: Use branch history to make better predictions
5. **Delayed Branches**: Always execute the instruction after the branch (branch delay slot)

**MIPS Handling of Control Hazards:**
- MIPS traditionally uses branch delay slots (one instruction after branch always executes)
- Modern MIPS implementations also use branch prediction

#### C. Structural Hazards

Structural hazards occur when multiple instructions need the same hardware resource simultaneously.

**Common Structural Hazards:**
1. **Memory Conflicts**: Instruction and data accesses to same memory
2. **Register File Conflicts**: Read and write in same cycle
3. **Execution Unit Conflicts**: Multiple instructions needing same functional unit

**MIPS Handling of Structural Hazards:**
- **Separate Instruction and Data Memories**: Eliminates memory conflict
- **Double-Ported Register File**: Allows simultaneous read/write
- **Pipeline Scheduling**: Ensures no resource conflicts

### 3.3 Forwarding Mechanism

#### Forwarding Paths
1. **EX/MEM to EX**: Forward ALU result to next instruction's ALU input
2. **MEM/WB to EX**: Forward memory result or ALU result to ALU input
3. **MEM/WB to MEM**: Forward result to memory stage (less common)

#### Forwarding Conditions in MIPS
For forwarding from EX/MEM to EX (ALU output to next ALU input):
```
if (EX/MEM.RegWrite
    and (EX/MEM.RegisterRd ≠ 0)
    and (EX/MEM.RegisterRd = ID/EX.RegisterRs))
then ForwardA = 10

if (EX/MEM.RegWrite
    and (EX/MEM.RegisterRd ≠ 0)
    and (EX/MEM.RegisterRd = ID/EX.RegisterRt))
then ForwardB = 10
```

For forwarding from MEM/WB to EX:
```
if (MEM/WB.RegWrite
    and (MEM/WB.RegisterRd ≠ 0)
    and (MEM/WB.RegisterRd = ID/EX.RegisterRs))
then ForwardA = 01

if (MEM/WB.RegWrite
    and (MEM/WB.RegisterRd ≠ 0)
    and (MEM/WB.RegisterRd = ID/EX.RegisterRt))
then ForwardB = 01
```

#### Data Paths Used for Forwarding
- **ALU Result Path**: EX/MEM.ALUResult → ALU input A or B
- **Memory Result Path**: MEM/WB.MemoryData → ALU input A or B
- **Register Value Path**: MEM/WB.ALUResult → ALU input A or B

### 3.4 Stalling Mechanism

#### When Forwarding Can't Help
The classic case where forwarding cannot resolve a hazard is the **load-use hazard**:
```
lw $t0, 0($t1)     # Load from memory to $t0
add $t2, $t0, $t3  # Try to use $t0 immediately after load
```

This requires a stall because:
1. Load instruction doesn't produce its result until after the MEM stage
2. The following add needs this value in its EX stage
3. By the time the load reaches the MEM stage, the add is already in EX
4. No forwarding path exists from MEM stage of one instruction to EX stage of the instruction right behind it

#### How Stalling Works
1. **Hazard Detection Unit**: Detects the load-use hazard condition
2. **Pipeline Control**: Inserts a bubble between load and using instruction
3. **PC and IF/ID Register**: Held constant for one cycle
4. **Control Signals**: Set to zero to create a NOP in the pipeline

#### Stalling Condition
```
if (ID/EX.MemRead
    and ((ID/EX.RegisterRt = IF/ID.RegisterRs)
         or (ID/EX.RegisterRt = IF/ID.RegisterRt)))
then Stall the pipeline
```

#### Data Paths Exercised During Stall
- **PC Register**: Disable write to keep PC constant
- **IF/ID Register**: Disable write to keep instruction
- **ID/EX Register**: Insert NOP by clearing control signals
- **Forwarding Unit**: Bypassed during stall cycle
- **Pipeline Bubble**: Propagated through EX, MEM, WB stages

## 4. Branch Prediction

### 4.1 Branch Prediction Fundamentals

#### Why Branch Prediction Matters
- **Pipeline Disruption**: Branches change the flow of instructions
- **Frequency**: 15-25% of instructions in typical programs are branches
- **Penalty**: Mispredicted branches waste 2+ cycles in 5-stage pipeline, more in deeper pipelines
- **Performance Impact**: With 20% branch frequency and 10% misprediction rate, CPI increases by 0.06 in a 5-stage pipeline

#### Basic Prediction Strategies
1. **Always Predict Not Taken**: Continue sequential execution
2. **Always Predict Taken**: Always fetch from branch target
3. **Static Prediction by Direction**: Backward branches (loops) predicted taken, forward branches predicted not taken
4. **1-bit Predictor**: Remember last outcome for each branch
5. **2-bit Predictor**: Use counters with hysteresis (needs two mispredictions to change prediction)

### 4.2 2-Bit Saturating Counter Predictor

#### State Diagram
```
                 Taken                   Taken
     ┌───────────────────────────┐ ┌───────────────────────────┐
     │                           ▼ │                           ▼
┌────┴─────┐                ┌────┴─────┐                ┌────┬─────┐
│  Strongly │    Not Taken   │   Weakly  │    Not Taken   │   Weakly  │
│ Not Taken │───────────────▶│ Not Taken │───────────────▶│   Taken   │
└────┬─────┘                └────┬─────┘                └────┬─────┘
     │                           ▲ │                           ▲
     └───────────────────────────┘ └───────────────────────────┘
                 Taken                   Not Taken
```

#### State Encoding
- **00**: Strongly Not Taken
- **01**: Weakly Not Taken
- **10**: Weakly Taken
- **11**: Strongly Taken

#### Advantages of 2-bit Prediction
- **Hysteresis**: Prevents thrashing on occasional mispredictions
- **Loop Handling**: Good for loops (first iteration predicted wrong, subsequent iterations correct)
- **Implementation**: Simple circuitry requiring only 2 bits per branch

### 4.3 Advanced Branch Prediction

#### Correlating Predictors
Use the outcome of previous branches to predict current branch (exploits patterns).

**Example**: 2-bit Global History with 2-bit Counters
- Track the outcome of last two branches (four possible patterns: TT, TN, NT, NN)
- Use separate 2-bit counter for each pattern
- Significantly better for branches that depend on other branches

#### Branch Target Buffer (BTB)
- Cache-like structure that stores:
  - Branch instruction address
  - Predicted target address
  - Prediction bits
- Allows predicted target address to be available early in the pipeline
- Critical for high-performance pipelining

#### Tournament Predictors
- Use multiple predictors in parallel
- Meta-predictor chooses which one to trust
- Adapts to different branch behaviors

### 4.4 Impact on Performance

#### Calculating Performance Impact
1. **Misprediction Rate**: Percentage of branches predicted incorrectly
2. **Branch Frequency**: Percentage of instructions that are branches
3. **Misprediction Penalty**: Cycles wasted per misprediction
4. **CPI Impact** = Branch Frequency × Misprediction Rate × Penalty

#### Example Calculation
For a processor with:
- 20% branch instructions
- 10% misprediction rate
- 3-cycle penalty

CPI Impact = 0.20 × 0.10 × 3 = 0.06
Effective CPI = Base CPI + 0.06

If base CPI is 1.0, this represents a 6% performance reduction.

## 5. Assembly Implementation of Stack Operations

### 5.1 Stack Concept in MIPS

#### Stack Principles
- Stack grows downward in memory (from high to low addresses)
- Stack pointer ($sp) points to the top of the stack
- Push: Decrement $sp, then store
- Pop: Load, then increment $sp

#### MIPS Register Conventions
- **$sp ($29)**: Stack pointer
- **$fp ($30)**: Frame pointer (optional)
- **$ra ($31)**: Return address
- **$s0-$s7**: Saved registers (preserved across calls)
- **$t0-$t9**: Temporary registers (not preserved)

### 5.2 Implementing Push Operation

#### Push a Register
```assembly
# Push $t0 onto the stack
addi $sp, $sp, -4    # Decrement stack pointer by 4 bytes
sw   $t0, 0($sp)     # Store $t0 at the new top of stack
```

#### Push Multiple Registers
```assembly
# Push $t0, $t1, $t2 onto the stack
addi $sp, $sp, -12   # Make space for 3 words
sw   $t0, 8($sp)     # Store $t0
sw   $t1, 4($sp)     # Store $t1
sw   $t2, 0($sp)     # Store $t2
```

#### Custom Push Instruction Implementation (Single-Cycle)

Implementing a `push $rt` instruction that pushes register $rt onto the stack:

**RTL Description**:
```
$sp ← $sp - 4
Memory[$sp] ← $rt
```

**Machine Code Format** (I-type):
```
| opcode (6 bits) | rs=29 (5 bits) | rt (5 bits) | immediate=4 (16 bits) |
```

**Datapath Modifications**:
1. Add ALU operation to decrement $sp by 4
2. Add path to store the updated $sp back to register file
3. Add path to use $rt as data for memory write
4. Add control signals for the new operation

**Control Signals**:
- ALUOp = Subtraction
- ALUSrc = 1 (use immediate value 4)
- RegWrite = 1 (write updated $sp)
- MemWrite = 1 (write to memory)
- Special control for register address selection

### 5.3 Implementing Pop Operation

#### Pop a Register
```assembly
# Pop from stack into $t0
lw   $t0, 0($sp)     # Load value from top of stack
addi $sp, $sp, 4     # Increment stack pointer by 4 bytes
```

#### Pop Multiple Registers
```assembly
# Pop into $t0, $t1, $t2 from the stack
lw   $t2, 0($sp)     # Load $t2
lw   $t1, 4($sp)     # Load $t1
lw   $t0, 8($sp)     # Load $t0
addi $sp, $sp, 12    # Adjust stack pointer
```

#### Custom Pop Instruction Implementation (Multi-Cycle)

Implementing a `pop $rt` instruction in multi-cycle MIPS:

**RTL Description**:
```
$rt ← Memory[$sp]
$sp ← $sp + 4
```

**State Sequence**:
1. **Fetch**: PC → Instruction Memory → IR
2. **Decode**: Identify pop instruction
3. **Memory Address**: Calculate memory address from $sp
4. **Memory Read**: Read from memory at address in $sp
5. **Write Back**: Write memory data to $rt
6. **Update $sp**: Increment $sp by 4

**Control Signals per State**:
- State 3: ALUSrcA = 1 (use $sp), ALUSrcB = 00 (use Register B), ALUOp = 00 (add)
- State 4: IorD = 1 (use ALU result for memory address), MemRead = 1
- State 5: RegDst = 01 (use rt field), RegWrite = 1, MemtoReg = 1
- State 6: ALUSrcA = 1 (use $sp), ALUSrcB = 01 (constant 4), ALUOp = 00 (add), RegDst = 11 (select $sp), RegWrite = 1, MemtoReg = 0

## 6. Custom Instruction Design

### 6.1 General Process for Adding Instructions

1. **Define Semantics**: What does the instruction do?
2. **Choose Instruction Format**: R-type, I-type, or J-type
3. **Design Datapath**: What hardware components are needed?
4. **Define Control Signals**: What control signals are needed?
5. **Verify Correctness**: Ensure the instruction works as expected

### 6.2 Example: Implementing a Custom Instruction

Let's implement a "Jump and Increment Register" (JIR) instruction that:
1. Jumps to the address in register rs
2. Increments register rt by 1

#### A. Instruction Format
Using R-type format:
```
| opcode (6 bits) | rs (5 bits) | rt (5 bits) | rd (unused) | shamt (unused) | funct (6 bits) |
|     000000      |    sssss    |    ttttt    |    00000    |     00000      |     101101     |
```

#### B. Single-Cycle Implementation

**RTL Description**:
```
PC ← $rs
$rt ← $rt + 1
```

**Datapath Requirements**:
1. Path to route $rs value to PC
2. ALU operation to increment $rt
3. Path to write back incremented value to register file
4. Control signals to manage both operations simultaneously

**Datapath Modifications**:
1. Add multiplexer to select $rs as PC input
2. Use ALU to compute $rt + 1
3. Add control logic to enable both PC update and register write

**Control Signals**:
- PCSource = 10 (new value to select $rs as source)
- RegWrite = 1 (enable register write)
- ALUSrc = 1 (use immediate value 1)
- RegDst = 01 (select rt as destination register)
- ALUOp = 00 (addition)

#### C. Multi-Cycle Implementation

**State Sequence**:
1. **Fetch**: Normal instruction fetch
2. **Decode**: Identify JIR instruction
3. **Execute**:
   - Route $rs to PC input path
   - Calculate $rt+1 in ALU
4. **Write Back**:
   - Update PC with $rs value
   - Write ALU result to $rt

**Control Signals per State**:
- State 3: ALUSrcA = 1 (use Register A = $rs), PCSource = 10 (from ALU), PCWrite = 1
- State 4: ALUSrcA = 1 (use Register B = $rt), ALUSrcB = 01 (constant 1), ALUOp = 00 (add)
- State 5: RegDst = 01 (use rt field), RegWrite = 1, MemtoReg = 0 (from ALU)

### 6.3 Challenges in Custom Instruction Design

#### Design Constraints
1. **Encoding Space**: Limited opcode/function code space
2. **Datapath Limitations**: Working within existing paths
3. **Control Complexity**: Managing multiple operations
4. **Pipeline Considerations**: Potential for new hazards
5. **Backward Compatibility**: Maintaining existing instructions

#### Design Tradeoffs
1. **Performance vs. Complexity**: Complex instructions may improve code density but complicate hardware
2. **Specialized vs. General**: Highly specialized instructions have limited use cases
3. **Single-Cycle vs. Multi-Cycle**: Complex operations may require multiple cycles
4. **Hardware vs. Software**: Some operations better implemented in software

## 7. Branch Prediction

### 7.1 Branch Prediction Fundamentals

#### Why Branch Prediction Matters
- **Pipeline Disruption**: Branches change the flow of instructions
- **Frequency**: 15-25% of instructions in typical programs are branches
- **Penalty**: Mispredicted branches waste 2+ cycles in 5-stage pipeline, more in deeper pipelines
- **Performance Impact**: With 20% branch frequency and 10% misprediction rate, CPI increases by 0.06 in a 5-stage pipeline

#### Basic Prediction Strategies
1. **Always Predict Not Taken**: Continue sequential execution
2. **Always Predict Taken**: Always fetch from branch target
3. **Static Prediction by Direction**: Backward branches (loops) predicted taken, forward branches predicted not taken
4. **1-bit Predictor**: Remember last outcome for each branch
5. **2-bit Predictor**: Use counters with hysteresis (needs two mispredictions to change prediction)

### 7.2 2-Bit Saturating Counter Predictor

#### State Diagram
```
                 Taken                   Taken
     ┌───────────────────────────┐ ┌───────────────────────────┐
     │                           ▼ │                           ▼
┌────┴─────┐                ┌────┴─────┐                ┌────┬─────┐
│  Strongly │    Not Taken   │   Weakly  │    Not Taken   │   Weakly  │
│ Not Taken │───────────────▶│ Not Taken │───────────────▶│   Taken   │
└────┬─────┘                └────┬─────┘                └────┬─────┘
     │                           ▲ │                           ▲
     └───────────────────────────┘ └───────────────────────────┘
                 Taken                   Not Taken
```

#### State Encoding
- **00**: Strongly Not Taken
- **01**: Weakly Not Taken
- **10**: Weakly Taken
- **11**: Strongly Taken

#### Advantages of 2-bit Prediction
- **Hysteresis**: Prevents thrashing on occasional mispredictions
- **Loop Handling**: Good for loops (first iteration predicted wrong, subsequent iterations correct)
- **Implementation**: Simple circuitry requiring only 2 bits per branch

### 7.3 Advanced Branch Prediction

#### Correlating Predictors
Use the outcome of previous branches to predict current branch (exploits patterns).

**Example**: 2-bit Global History with 2-bit Counters
- Track the outcome of last two branches (four possible patterns: TT, TN, NT, NN)
- Use separate 2-bit counter for each pattern
- Significantly better for branches that depend on other branches

#### Branch Target Buffer (BTB)
- Cache-like structure that stores:
  - Branch instruction address
  - Predicted target address
  - Prediction bits
- Allows predicted target address to be available early in the pipeline
- Critical for high-performance pipelining

#### Tournament Predictors
- Use multiple predictors in parallel
- Meta-predictor chooses which one to trust
- Adapts to different branch behaviors

### 7.4 Impact on Performance

#### Calculating Performance Impact
1. **Misprediction Rate**: Percentage of branches predicted incorrectly
2. **Branch Frequency**: Percentage of instructions that are branches
3. **Misprediction Penalty**: Cycles wasted per misprediction
4. **CPI Impact** = Branch Frequency × Misprediction Rate × Penalty

#### Example Calculation
For a processor with:
- 20% branch instructions
- 10% misprediction rate
- 3-cycle penalty

CPI Impact = 0.20 × 0.10 × 3 = 0.06
Effective CPI = Base CPI + 0.06

If base CPI is 1.0, this represents a 6% performance reduction.

## Summary of Key Takeaways

1. **Architecture Choice Depends on Needs**:
   - Single-cycle for simplicity
   - Multi-cycle for balanced performance and resource usage
   - Pipelined for high throughput
   - Microcoded for complex instructions

2. **Performance Analysis Requires**:
   - Understanding instruction mix
   - Calculating critical paths
   - Accounting for hazards and stalls
   - Balancing throughput and latency

3. **Pipeline Hazards Require Solutions**:
   - Data hazards: forwarding and stalling
   - Control hazards: prediction and delay slots
   - Structural hazards: resource duplication

4. **MIPS Forwarding Works When**:
   - Data produced in one instruction
   - Needed by a later instruction
   - Result available in pipeline register
   - Valid forwarding path exists

5. **MIPS Stalling Needed When**:
   - Load-use hazards occur
   - No valid forwarding path exists
   - Hardware detects hazard and freezes pipeline

6. **Branch Prediction Critical for Performance**:
   - Simple predictors work well for most code
   - More advanced predictors for complex branching patterns
   - Misprediction penalty increases with pipeline depth
