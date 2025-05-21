# CSCI 260: Inferred Exam with Complete Solutions

## Question 1: Processor Architecture Latency Comparison (15 points)

### Question:
Compare the latency characteristics of single-cycle, multi-cycle, pipelined, and microcoded MIPS architectures by answering the following:

a) Which architecture has the longest latency for executing the longest/most complex instruction (such as a load word)? Explain why.

b) Which architecture has the longest latency for executing the shortest/simplest instruction (such as an R-type add)? Explain why.

c) For each architecture, explain the relationship between instruction complexity and execution time.

### Solution:

#### Part a) Longest latency for complex instructions
**Answer: Single-cycle architecture**

**Explanation:** In a single-cycle architecture, all instructions must complete in a single clock cycle, so the clock period must accommodate the slowest/most complex instruction (typically load word). Since the clock period is fixed at the longest path delay, complex instructions like load word directly determine the execution time. For a load word instruction, the critical path includes PC read → Instruction memory → Register file read → ALU (address calculation) → Data memory read → Register file write, resulting in the longest possible latency.

The multi-cycle splits this into steps, microcoded architecture breaks it into even smaller microoperations, and pipelined architecture overlaps execution, all resulting in lower latency for an individual complex instruction.

#### Part b) Longest latency for simple instructions
**Answer: Single-cycle architecture**

**Explanation:** In a single-cycle architecture, even the simplest instructions (like R-type arithmetic operations) must use the same clock period as the most complex instructions. This means that simple instructions are significantly slowed down because they must wait for the entire clock period determined by the complex instructions.

For example, an R-type add instruction in a single-cycle architecture would take the same time as a load word instruction, despite not needing data memory access. In multi-cycle and microcoded architectures, simple instructions use fewer cycles/micro-operations, and in pipelined architectures, they flow through the pipeline with minimal stalls.

#### Part c) Relationship between instruction complexity and execution time

**Single-cycle:**
- All instructions take exactly the same time to execute
- Execution time = clock period (determined by the most complex instruction)
- No relationship between instruction complexity and execution time once implemented

**Multi-cycle:**
- Different instructions take different numbers of cycles
- Execution time = (number of cycles for instruction) × (clock period)
- Direct relationship between instruction complexity and execution time
- Simple instructions (R-type): ~4 cycles
- Complex instructions (load/store): ~5 cycles
- Clock period is determined by the longest individual stage

**Pipelined:**
- Ideal execution rate is 1 instruction per cycle once pipeline is filled
- Execution time affected by hazards, which are more common with complex instructions
- Relationship is weak for individual instructions but strong for sequences of instructions
- Complex instructions may cause more pipeline stalls

**Microcoded:**
- Each instruction broken into variable number of microcode steps
- Execution time = (number of microinstructions) × (microinstruction cycle time)
- Very direct relationship between instruction complexity and execution time
- Complex instructions require many more microinstructions than simple ones

## Question 2: Pipeline Performance Analysis (15 points)

### Question:
Consider two different pipeline implementations:
- Pipeline A: 4ns clock period with 16 pipeline stages
- Pipeline B: 5ns clock period with 10 pipeline stages

a) Which pipeline would you expect to have better throughput? Explain your reasoning.

b) Calculate the theoretical maximum throughput (in instructions per second) for both pipelines.

c) If a branch misprediction flushes the entire pipeline and branch instructions constitute 20% of the instruction mix with a prediction accuracy of 90%, calculate the effective throughput for both pipelines.

### Solution:

#### Part a) Expected better throughput
**Answer: It depends, but likely Pipeline A**

**Explanation:** Throughput is determined by how many instructions complete per unit time. In an ideal pipeline with no hazards:

- Pipeline A: 1 instruction every 4ns (once pipeline is full)
- Pipeline B: 1 instruction every 5ns (once pipeline is full)

Pipeline A has a shorter clock period (4ns vs 5ns), suggesting higher throughput. However, the longer pipeline (16 stages vs 10) means A will suffer more from hazards, branch mispredictions, and pipeline stalls. Additionally, startup time is longer for Pipeline A. For very short programs, Pipeline B might perform better, but for longer programs, Pipeline A would likely have better throughput.

#### Part b) Theoretical maximum throughput
**Pipeline A:**
- Throughput = 1 instruction per cycle / clock period
- Throughput = 1 / 4ns = 0.25 instructions/ns = 250 million instructions/second = 250 MIPS

**Pipeline B:**
- Throughput = 1 instruction per cycle / clock period
- Throughput = 1 / 5ns = 0.2 instructions/ns = 200 million instructions/second = 200 MIPS

Pipeline A has a theoretical throughput advantage of 25% over Pipeline B.

#### Part c) Effective throughput with branch mispredictions

For a branch misprediction, the entire pipeline must be flushed, resulting in a penalty equal to the number of pipeline stages:

**Pipeline A:**
- Misprediction rate = 20% (branch frequency) × 10% (1 - prediction accuracy) = 2%
- Misprediction penalty = 16 cycles
- Average CPI = 1 + (0.02 × 16) = 1 + 0.32 = 1.32
- Effective throughput = 250 MIPS / 1.32 = 189.4 MIPS

**Pipeline B:**
- Misprediction rate = 20% (branch frequency) × 10% (1 - prediction accuracy) = 2%
- Misprediction penalty = 10 cycles
- Average CPI = 1 + (0.02 × 10) = 1 + 0.2 = 1.2
- Effective throughput = 200 MIPS / 1.2 = 166.7 MIPS

Pipeline A still has higher effective throughput (189.4 MIPS vs 166.7 MIPS), but the advantage has decreased from 25% to about 13.6% due to the longer pipeline's greater vulnerability to branch misprediction penalties.

## Question 3: Number Representation (15 points)

### Question:
a) Convert the decimal number 6.75 to a 16-bit fixed-point representation with 8 bits for the integer part and 8 bits for the fractional part (Q8.8 format). Show your work.

b) Convert the decimal number 41.625 to 16-bit floating point format (1 sign bit, 5 exponent bits with bias of 15, 10 mantissa bits). Show your work.

c) What is the next largest number after -3 that can be represented exactly in the 16-bit floating point format described in part b? Show your work.

### Solution:

#### Part a) Fixed-point representation of 6.75
**Step 1: Convert the integer part to binary**
6₁₀ = 110₂

**Step 2: Convert the fractional part to binary**
0.75₁₀ = 0.75 × 2 = 1.5 → 1
         0.5 × 2 = 1.0 → 1
0.75₁₀ = 0.11₂

**Step 3: Combine and pad to required format**
6.75₁₀ = 110.11₂
Q8.8 representation:
- Integer part (8 bits): 00000110
- Fractional part (8 bits): 11000000

**Answer: 0000011011000000 (0x0CC0)**

#### Part b) 16-bit floating point representation of 41.625

**Step 1: Convert to binary**
41₁₀ = 101001₂
0.625₁₀ = 0.101₂
41.625₁₀ = 101001.101₂

**Step 2: Normalize**
101001.101₂ = 1.01001101 × 2^5

**Step 3: Determine sign, exponent, and fraction**
- Sign bit: 0 (positive)
- Exponent: 5 + bias(15) = 20 = 10100₂
- Mantissa: 01001101 padded to 10 bits = 0100110100

**Step 4: Assemble**
0 10100 0100110100

**Answer: 0101000100110100 (0x5136)**

#### Part c) Next largest number after -3 in 16-bit floating point

**Step 1: Represent -3 in 16-bit floating point**
3₁₀ = 11₂ = 1.1 × 2^1
- Sign bit: 1 (negative)
- Exponent: 1 + bias(15) = 16 = 10000₂
- Mantissa: 1 (implied) followed by 0 bits = 1000000000

-3 in 16-bit floating point: 1 10000 0000000000

**Step 2: Find the next representable number**
In floating point, the next larger number is found by incrementing the mantissa by its least significant bit:
1 10000 0000000001

**Step 3: Convert back to decimal**
- Sign: 1 (negative)
- Exponent: 10000₂ = 16, unbiased = 16 - 15 = 1
- Mantissa: 0000000001 → with implied leading 1 → 1.0000000001₂

Value = -1 × 1.0000000001₂ × 2^1
      = -1 × (2 + 2^(-10))
      = -1 × (2 + 0.0009765625)
      = -1 × 2.0009765625
      = -2.0009765625

**Answer: -2.0009765625**

This is the next representable number larger than -3 (moving toward zero) in this format.

## Question 4: Custom Instruction Implementation (15 points)

### Question:
Implement a new custom MIPS instruction called "JIR" (Jump and Increment Register) that performs the following operations:
1. Jumps to the address stored in register rs
2. Increments the value in register rt by 1

Specifically:
a) Define the machine code format for this instruction, including opcode and function code (if applicable).

b) Describe the datapath modifications required to implement this instruction in a single-cycle MIPS processor. Include any new control signals or hardware components needed.

c) Complete the control signal settings for this new instruction in the MIPS control table.

d) Explain how the processor will execute this instruction step-by-step.

### Solution:

#### Part a) Machine code format

Since this instruction involves two registers but no immediate value, I'll use an R-type format:

```
| opcode (6 bits) | rs (5 bits) | rt (5 bits) | rd (5 bits) | shamt (5 bits) | funct (6 bits) |
|      000000     |    sssss    |    ttttt    |    00000    |     00000      |    001101      |
```

- Opcode: 000000 (R-type)
- rs: address to jump to
- rt: register to increment
- rd: unused (set to 00000)
- shamt: unused (set to 00000)
- funct: 001101 (unique function code for JIR)

#### Part b) Datapath modifications

The JIR instruction requires the following modifications to the standard MIPS single-cycle datapath:

1. A new control signal `IncReg` that enables incrementing of register rt
2. A new ALU operation for incrementing (or reuse the existing addition operation)
3. A multiplexer to select between the normal ALU result and the incremented value
4. A path to allow setting the PC from the register value
5. An adder or ALU operation to compute rt+1
6. Logic to enable both register write and PC update in the same cycle

The key challenge is that this instruction must both update a register and change the PC in the same cycle, which requires additional paths and control logic.

#### Part c) Control signals for JIR

| Control Signal | Value | Explanation |
|----------------|-------|-------------|
| RegDst         | X     | Don't care (rt is specified in instruction) |
| ALUSrc         | 0     | Use register value (for incrementing rt) |
| MemtoReg       | 0     | ALU result to register (not memory) |
| RegWrite       | 1     | Need to write back to register rt |
| MemRead        | 0     | No memory read |
| MemWrite       | 0     | No memory write |
| Branch         | 0     | Not a branch (using Jump mechanism) |
| ALUOp          | 10    | ALU performs addition for increment |
| PCSource       | 10    | New control signal value for register source |
| Jump           | 0     | Not using standard jump mechanism |
| IncReg         | 1     | New control signal to increment register |
| JumpReg        | 1     | New control signal to jump to register value |

#### Part d) Execution steps

1. **Fetch**: PC → Instruction Memory → Instruction Register
2. **Decode**: 
   - Control unit recognizes JIR instruction (opcode 000000, funct 001101)
   - Register file reads rs (address to jump to) and rt (register to increment)
3. **Execute**:
   - ALU calculates rt+1 (increment operation)
   - In parallel, the value from rs is prepared for the PC
4. **Memory**: No memory operation for this instruction
5. **Write Back**:
   - The incremented value (rt+1) is written back to register rt in the register file
   - In parallel, the PC is updated with the value from rs

This instruction is similar to the Jump Register (JR) instruction but adds the register increment functionality. It's also similar to the Jump and Link (JAL) instruction in that it both updates a register and the PC, but it uses a register value for the jump target instead of an immediate address.

## Question 5: Multi-Cycle Instruction Implementation (15 points)

### Question:
Design a multi-cycle implementation to add the values in registers x, y, and z and store the result in register x. Specifically:

a) Write the RTL (Register Transfer Language) description for this operation.

b) Design the machine code format for a custom instruction that performs this operation, including opcode and any necessary fields.

c) Show the sequence of steps (states) required to implement this instruction in a multi-cycle MIPS processor, including all control signals for each step.

d) Describe any modifications needed to the standard multi-cycle MIPS datapath to support this instruction.

### Solution:

#### Part a) RTL description

```
R[x] ← R[x] + R[y] + R[z]
```

This RTL describes adding the contents of registers x, y, and z and storing the result back in register x.

#### Part b) Machine code format

Since this instruction requires three register operands (x, y, and z), an R-type format is most appropriate:

```
| opcode (6 bits) | rs (5 bits) | rt (5 bits) | rd (5 bits) | shamt (5 bits) | funct (6 bits) |
|      000000     |  x (sssss)  |  y (ttttt)  |  z (rrrrr)  |     00000      |    101010      |
```

- Opcode: 000000 (R-type)
- rs: register x (first operand and destination)
- rt: register y (second operand)
- rd: register z (third operand)
- shamt: unused (set to 00000)
- funct: 101010 (unique function code for ADD3)

The instruction could be called "ADD3" for "Add Three Registers".

#### Part c) Multi-cycle implementation steps

**State 1: Instruction Fetch**
- IorD = 0 (memory address from PC)
- IRWrite = 1 (write instruction to IR)
- ALUSrcA = 0 (ALU input A from PC)
- ALUSrcB = 01 (ALU input B is 4)
- ALUOp = 00 (ALU performs addition)
- PCWrite = 1 (update PC)
- PCSource = 00 (next PC from ALU result)

**State 2: Instruction Decode / Register Fetch**
- ALUSrcA = 0 (not used in this state)
- ALUSrcB = 11 (not used in this state)
- ALUOp = 00 (not used in this state)

**State 3: First Addition (x + y)**
- ALUSrcA = 1 (ALU input A from register x)
- ALUSrcB = 00 (ALU input B from register y)
- ALUOp = 10 (ALU performs addition)
- Store result in ALUOUT register

**State 4: Second Addition (ALUOUT + z)**
- ALUSrcA = 0 (ALU input A from ALUOUT)
- ALUSrcB = 10 (ALU input B from register z)
- ALUOp = 10 (ALU performs addition)
- Store result in ALUOUT register

**State 5: Write Back to Register x**
- RegDst = 00 (destination register is rs field)
- RegWrite = 1 (enable register writing)
- MemtoReg = 0 (write ALU result to register)

#### Part d) Datapath modifications

The standard multi-cycle MIPS datapath needs these modifications:

1. **Additional Multiplexer for ALUSrcA**: The existing ALUSrcA mux needs to be expanded to select from PC, Register A, and ALUOUT.

2. **Modified Control for Register Destination**: A new control signal for RegDst that allows selecting the rs field as the destination register (rather than the standard rt or rd).

3. **Modified ALUSrcB Control**: The existing ALUSrcB mux needs to be expanded to select Register B for the second operand and a new path for Register C (z).

4. **Additional State in Control FSM**: The control state machine needs a new state for the second addition operation.

5. **Additional Register**: A Register C to hold the value from z (in addition to the standard A and B registers).

The key modification is adding support for a third register operand and being able to perform two consecutive ALU operations on three inputs. The datapath also needs to be able to write the result back to the register specified in the rs field rather than the standard rt or rd fields.

## Question 6: MIPS Instruction from Datapath Diagram (15 points)

### Question:
Figure 4.57 from your textbook (shown below) displays a close-up of a MIPS datapath with a 2:1 multiplexer added to select the signed immediate as an ALU input. Based on this diagram, answer the following questions:

![Figure 4.57: A close-up of the datapath showing a 2:1 multiplexer for selecting signed immediate as ALU input]

a) What MIPS instruction is this datapath designed to implement? Describe the operation in both English and RTL notation.

b) Write the machine code format for this instruction, showing all fields and their sizes.

c) Write an example of this instruction in MIPS assembly language, and show the corresponding machine code in hexadecimal.

d) Explain how the datapath executes this instruction step-by-step, including the role of each component shown in the diagram.

### Solution:

#### Part a) Instruction identification and description

The diagram shows a datapath modified to handle I-type instructions that use immediate values as one of the ALU inputs. This is evident from the highlighted 2:1 multiplexer (ALUSrc) that selects between a register value and a sign-extended immediate value.

While this datapath supports multiple I-type instructions, the most common and representative instruction is the **Load Word (LW)** instruction.

**Operation in English**: Load Word loads a 32-bit word from memory at the address calculated by adding a sign-extended 16-bit immediate offset to the contents of a base register (rs), and places the result in register rt.

**RTL Notation**: R[rt] ← Memory[R[rs] + SignExt(immediate)]

#### Part b) Machine code format

The Load Word (LW) instruction uses the I-type format:

```
| opcode (6 bits) | rs (5 bits) | rt (5 bits) | immediate (16 bits) |
|     100011      |    sssss    |    ttttt    |   iiiiiiiiiiiiiiii  |
```

- Opcode: 100011 (35 in decimal) - identifies this as a LW instruction
- rs: 5-bit base register address (source for memory address calculation)
- rt: 5-bit destination register address (where loaded data will be stored)
- immediate: 16-bit offset value (sign-extended for address calculation)

#### Part c) Example instruction and machine code

**MIPS Assembly**:
```
lw $t0, 8($s0)   # Load word from memory at address $s0+8 into register $t0
```

**Machine Code**:
- Opcode: 100011 (LW)
- rs: $s0 = 10000 (register 16)
- rt: $t0 = 01000 (register 8)
- immediate: 8 = 0000000000001000

Binary: 10001110000010000000000000001000
Hexadecimal: 0x8E080008

#### Part d) Execution step-by-step

The execution of a Load Word instruction in the pipelined datapath shown proceeds through the following steps:

1. **Instruction Fetch (IF) Stage** (not shown in this diagram):
   - The instruction is fetched from instruction memory
   - The PC is incremented

2. **Instruction Decode (ID) Stage**:
   - The instruction is decoded, identifying it as LW
   - Control signals are generated, including setting ALUSrc = 1 to select the immediate value
   - Register values are read from the register file (rs for base address)
   - The 16-bit immediate value is sign-extended to 32 bits
   - All values are passed to the ID/EX pipeline register

3. **Execute (EX) Stage**:
   - The ALUSrc multiplexer (highlighted in blue) selects the sign-extended immediate value
   - The ALU adds the base register value and immediate to calculate the memory address
   - The ALU result (memory address) and data to be stored are passed to the EX/MEM pipeline register

4. **Memory (MEM) Stage**:
   - The calculated address is sent to data memory
   - Data is read from memory at this address
   - The memory data and destination register information are passed to the MEM/WB pipeline register

5. **Write Back (WB) Stage**:
   - The MUX in the WB stage selects data from memory
   - This data is written back to the destination register (rt)

**Forwarding Unit Role**: The diagram shows a forwarding unit that monitors dependencies between instructions and can route data directly from the ALU output or memory output back to the ALU inputs, bypassing the register file when a value is needed before it has been written back.

The specific datapath elements from the diagram that play key roles:
- **ALUSrc Multiplexer**: Selects the immediate value instead of a register value as the second ALU input
- **Forwarding Multiplexers**: Allow bypassing the register file when data dependencies exist
- **ALU**: Computes the memory address by adding the base register value and the immediate offset
- **Data Memory**: Retrieves the data from the calculated address
- **Write-Back Multiplexer**: Selects the data from memory to be written to the register file

This implementation efficiently handles the LW instruction while supporting forwarding to minimize pipeline stalls due to data hazards.


## Question 7: Short Answer Questions (10 points)

### Question:
Answer each of the following short questions in 1-3 sentences:

a) Why does a multi-cycle MIPS architecture generally have a shorter clock period than a single-cycle architecture?

b) What is the primary advantage of a pipelined architecture over a multi-cycle architecture?

c) Why does branch prediction become more important as pipeline depth increases?

d) What is the difference between a structural hazard and a data hazard in pipelined processors?

e) How does microcoded control differ from hardwired control in processor design?

### Solution:

#### Part a) Multi-cycle vs. single-cycle clock period
In a multi-cycle architecture, the clock period is determined by the longest individual stage (e.g., ALU operation), whereas in a single-cycle architecture, the clock period must accommodate the entire longest instruction path (e.g., PC → IM → RF → ALU → DM → RF). By breaking instructions into multiple steps, the multi-cycle design can have a significantly shorter clock period.

#### Part b) Pipelined vs. multi-cycle advantage
The primary advantage of a pipelined architecture over a multi-cycle architecture is throughput: while a multi-cycle architecture executes one instruction every multiple clock cycles, a pipelined architecture can ideally complete one instruction every single clock cycle once the pipeline is filled, by allowing multiple instructions to execute simultaneously in different pipeline stages.

#### Part c) Branch prediction importance in deeper pipelines
As pipeline depth increases, the penalty for a branch misprediction (number of wasted cycles) increases proportionally because more pipeline stages must be flushed and refilled. For example, in a 5-stage pipeline, a misprediction might waste 4 cycles, but in a 16-stage pipeline, it could waste 15 cycles, making effective branch prediction critical for maintaining performance.

#### Part d) Structural vs. data hazards
A structural hazard occurs when two instructions need to use the same hardware resource simultaneously (e.g., two instructions needing to access memory in the same cycle), while a data hazard occurs when an instruction depends on data produced by a previous instruction that hasn't yet completed (e.g., using a value that's still being calculated). Structural hazards are about resource conflicts, while data hazards are about data dependencies.

#### Part e) Microcoded vs. hardwired control
Microcoded control implements processor control logic using a microprogram stored in memory (control store) that executes microinstructions to generate control signals, while hardwired control implements control logic directly with combinational logic circuits. Microcoded control is more flexible and easier to modify but typically slower, while hardwired control is faster but less flexible and more difficult to design and modify.
