# Inferred Computer Architecture Exam Questions & Solutions

Based on the student's recollections, I've reconstructed what appears to be a computer architecture exam focusing on processor design, pipelining, instruction execution, and number representation. Below are the inferred complete questions with detailed solutions.

## Contents
1. [CPU Latency Comparison](#question-1-cpu-latency-comparison)
2. [Pipeline Throughput Calculation](#question-2-pipeline-throughput-calculation)
3. [Number Representation](#question-3-number-representation)
4. [Custom Instruction Implementation](#question-4-custom-instruction-implementation)
5. [Multicycle Operation](#question-5-multicycle-operation)
6. [MIPS Instruction Implementation](#question-6-mips-instruction-implementation)

## Question 1: CPU Latency Comparison

**Question:** Compare the latency of single-cycle, multicycle, pipeline, and microcode implementations of a processor. Which implementation has the longest latency with the longest instruction? Which has the longest latency with the shortest instruction?

**Solution:**

### Latency Comparison:

| Implementation | Latency Characteristic | Clock Cycle Time |
|----------------|------------------------|------------------|
| Single-Cycle   | Fixed latency for all instructions | Very long (limited by longest instruction) |
| Multicycle     | Variable latency based on instruction complexity | Medium (independent of longest instruction) |
| Pipeline       | Fixed latency after pipeline fills | Short |
| Microcode      | Highly variable latency based on instruction complexity | Medium |

### Longest Latency with Longest Instruction:
**Single-Cycle** has the longest latency for the longest instruction, since the clock cycle must accommodate the worst-case (longest) instruction path. If the longest instruction takes 5ns in raw propagation time, then all instructions must execute in 5ns (plus setup time and clock skew).

### Longest Latency with Shortest Instruction:
**Microcode** typically has the longest latency for the shortest instruction. Even simple instructions must go through microcode fetch and execution cycles, adding overhead for instruction decoding and sequencing.

**Explanation:**
- In a single-cycle implementation, all instructions complete in one cycle, but that cycle is very long (determined by the most complex instruction).
- In a multicycle implementation, different instructions take different numbers of cycles, with simple instructions requiring fewer cycles than complex ones.
- In a pipelined implementation, after the pipeline fills, instructions complete at the rate of one per cycle (ignoring hazards).
- In a microcoded implementation, each instruction is broken down into microcoded operations, which adds overhead particularly for simple instructions.

## Question 2: Pipeline Throughput Calculation

**Question:** Consider two pipeline designs: Design A with a 4ns clock cycle and 16 pipeline stages, and Design B with a 5ns clock cycle and 10 pipeline stages. Which design has better throughput? Calculate the throughput for each design.

**Solution:**

### Throughput Calculation:
Throughput = Instructions completed per second = 1 / (Clock cycle time)

For Design A:
- Clock cycle time = 4ns
- Throughput = 1 / (4 × 10^-9) = 250 million instructions per second (MIPS)

For Design B:
- Clock cycle time = 5ns
- Throughput = 1 / (5 × 10^-9) = 200 million instructions per second (MIPS)

**Design A has better throughput** at 250 MIPS compared to Design B's 200 MIPS.

### Additional Analysis:

1. **Latency Comparison**:
   - Design A latency = 4ns × 16 stages = 64ns per instruction
   - Design B latency = 5ns × 10 stages = 50ns per instruction
   
   While Design A has better throughput, Design B has lower latency per instruction.

2. **Practical Considerations**:
   - A deeper pipeline (Design A) is more susceptible to hazards
   - More pipeline stages means more pipeline registers and higher power consumption
   - Design B might be preferable for applications sensitive to instruction latency
   - Design A might be preferable for applications requiring maximum throughput

The choice between designs would depend on the specific requirements of the system, balancing throughput against latency and power considerations.

## Question 3: Number Representation

**Question:** Perform the following number representation tasks:

a) Translate the decimal number 13.625 into 16-bit fixed point representation, using 8 bits for the integer part and 8 bits for the fractional part.

b) Translate the decimal number 13.625 into IEEE 754 16-bit floating point format.

c) What is the next largest number after -3 that can be represented in 16-bit IEEE 754 floating point format?

**Solution:**

### a) Fixed Point Representation:

To represent 13.625 in 16-bit fixed point with 8.8 format:

1. Convert integer part (13) to binary:
   13₁₀ = 1101₂

2. Convert fractional part (0.625) to binary:
   0.625 × 2 = 1.25  → 1
   0.25 × 2 = 0.5    → 0
   0.5 × 2 = 1.0     → 1
   0.625₁₀ = 0.101₂

3. Combine: 13.625₁₀ = 1101.101₂

4. Format to 8.8 fixed point (padding with zeros):
   Integer part: 00001101 (8 bits)
   Fractional part: 10100000 (8 bits)

5. Final 16-bit fixed point representation: 0000110110100000

### b) 16-bit Floating Point Representation:

For IEEE 754 16-bit ("half precision") format:
- 1 sign bit
- 5 exponent bits (bias of 15)
- 10 mantissa bits

Steps:
1. Sign bit = 0 (positive)

2. Convert to normalized scientific notation:
   13.625₁₀ = 1.3625 × 10¹ in decimal
   13.625₁₀ = 1101.101₂ = 1.101101 × 2³ in binary

3. Exponent calculation:
   E = e + bias = 3 + 15 = 18₁₀ = 10010₂

4. Mantissa (store only the fractional part after the implicit 1):
   Fractional part = 101101 padded to 10 bits = 1011010000

5. Final 16-bit IEEE 754 representation:
   Sign (1 bit): 0
   Exponent (5 bits): 10010
   Mantissa (10 bits): 1011010000
   
   Result: 0100101011010000

### c) Next Largest Number After -3:

To find the next largest number after -3 in 16-bit floating point:

1. Represent -3 in IEEE 754 16-bit format:
   - Sign bit = 1 (negative)
   - -3₁₀ = -1.5 × 2¹ in binary scientific notation
   - Exponent = 1 + 15 = 16₁₀ = 10000₂
   - Mantissa = 1.1₂, but we store 1000000000 (implicit leading 1)
   - -3 in IEEE 754 16-bit = 1100001000000000

2. The next largest number would have a mantissa value one increment larger:
   - Change mantissa from 1000000000 to 1000000001
   - This gives: 1100001000000001

3. In decimal, this represents:
   - Sign: negative
   - Exponent: 16 - 15 = 1
   - Mantissa: 1.1000000001₂
   - Value = -1.1000000001₂ × 2¹ = -2.9997559...₁₀

Therefore, the next largest number after -3 is approximately -2.9998 in decimal.

## Question 4: Custom Instruction Implementation

**Question:** Implement a custom "Jump If Register" (JIR) instruction for a single-cycle MIPS processor. The instruction format should be:

JIR Rd, Rs
(Jump to the address in register Rd if register Rs is non-zero)

Describe the necessary datapath modifications and control signals required to implement this instruction.

**Solution:**

### JIR Instruction Specification:
- **Format**: R-type instruction
- **Operation**: If (Rs ≠ 0) then PC ← Rd
- **Encoding**:
  - opcode: 000000 (R-type)
  - rs: 5-bit source register
  - rd: 5-bit destination register (contains jump address)
  - shamt: 00000 (unused)
  - funct: 001011 (custom function code for JIR)

### Datapath Modifications:

1. **ALU Operation**: 
   - Configure ALU to test if Rs ≠ 0 (can use existing zero flag inverted)
   - Add a multiplexer to select between regular ALU output and this comparison

2. **Branch Control**:
   - Add a new control signal "JIRCtrl" that enables JIR functionality
   - Update PC input multiplexer to accept register value from Rd when JIR is active

3. **Control Path**:
   - Add logic to control unit to recognize JIR instruction by its opcode and function code
   - Generate appropriate control signals:
     * RegRead for both Rs and Rd
     * ALUOp to perform non-zero test
     * JIRCtrl signal to enable register-based jump

### Required Control Signals:

| Signal   | Purpose                                         | Value for JIR |
|----------|------------------------------------------------|---------------|
| RegRead  | Enable reading both Rs and Rd registers        | 1             |
| ALUOp    | Configure ALU for non-zero test                | Special code  |
| JIRCtrl  | Enable jump to register value                  | 1             |
| PCWrite  | Allow updating the program counter             | 1             |
| MemRead  | Memory read (not needed for JIR)               | 0             |
| MemWrite | Memory write (not needed for JIR)              | 0             |
| RegWrite | Register write (not needed for JIR)            | 0             |

### Implementation Diagram:

```
[Instruction Memory] → [Instruction Register] → [Control Unit] → JIRCtrl
                                             ↓
                     [Register File] → Rs → [ALU] → Zero Flag → NOT → [AND]
                                   ↓                                    ↑
                                   Rd ----------------→ [MUX] ← [PC+4]  |
                                                         ↓              |
                                                        [PC] ← ─────────┘
```

### Execution Steps:
1. Fetch instruction from instruction memory
2. Decode instruction, recognize JIR opcode/funct
3. Read values from registers Rs and Rd
4. Test if Rs ≠ 0
5. If true, load PC with value from Rd; otherwise, PC = PC+4

This implementation allows for a conditional jump to any address stored in a register, providing more flexibility than the standard MIPS conditional branches.

## Question 5: Multicycle Operation

**Question:** Given a multicycle implementation, write the sequence of operations required to add the values of registers x, y, and z, and store the result in register x.

**Solution:**

### Instruction: ADD x, y, z (x = x + y + z)

This would likely be implemented as multiple instructions in MIPS:
```
ADD temp, y, z   # temp = y + z
ADD x, x, temp   # x = x + temp
```

For this analysis, we'll assume a hypothetical instruction that performs this operation directly in a multicycle implementation.

### Multicycle Operation Sequence:

#### Cycle 1: Instruction Fetch (IF)
- PC → MAR
- Read memory at address in MAR
- MDR → IR (Instruction Register)
- PC = PC + 4

#### Cycle 2: Instruction Decode (ID)
- Decode instruction from IR
- Determine operation type (ADD) and register operands (x, y, z)
- Read register values: Reg[x] → A, Reg[y] → B

#### Cycle 3: First Execution (EX1)
- ALU performs A + B (x + y)
- Result stored in temporary register (Temp)

#### Cycle 4: Second Execution (EX2)
- Read register value: Reg[z] → B
- ALU performs Temp + B (x + y + z)
- Result stored in ALU output register

#### Cycle 5: Write Back (WB)
- ALU output → Reg[x]

### Register Transfer Level (RTL) Description:

```
# Cycle 1 (IF)
MAR ← PC
MDR ← Memory[MAR]
IR ← MDR
PC ← PC + 4

# Cycle 2 (ID)
A ← Reg[x]
B ← Reg[y]

# Cycle 3 (EX1)
Temp ← A + B

# Cycle 4 (EX2)
B ← Reg[z]
ALUOut ← Temp + B

# Cycle 5 (WB)
Reg[x] ← ALUOut
```

### Data Bubble Diagram:
```
     ┌─────┐     ┌─────┐     ┌─────┐     ┌─────┐     ┌─────┐
     │ IF  │ ──> │ ID  │ ──> │ EX1 │ ──> │ EX2 │ ──> │ WB  │
     └─────┘     └─────┘     └─────┘     └─────┘     └─────┘
PC → MAR      Decode IR    A + B → Temp  Temp + z   ALUOut → x
Memory → IR   x → A        
PC + 4 → PC   y → B        
```

This implementation requires 5 cycles to complete the operation. In a real processor, this might be implemented as a sequence of simpler instructions to avoid custom datapath modifications.

## Question 6: MIPS Instruction Implementation

**Question:** Given Figure 4.5.7 from the textbook, write the MIPS instruction(s) needed to implement the described functionality.

**Solution:**

Since the exact figure isn't provided, I'll infer a likely scenario from a typical MIPS textbook. Figure 4.5.7 likely shows a control flow or memory access pattern commonly covered in computer architecture textbooks.

### Inferred Figure Scenario: Branch with Offset Calculation

Assuming Figure 4.5.7 illustrates a branch operation where the target address is calculated by adding an offset to the current PC:

### Required MIPS Instruction:

```assembly
BEQ $t0, $zero, offset    # Branch if $t0 equals zero, to address (PC+4) + (offset<<2)
```

### Alternative Scenario: Memory Access with Base Register and Offset

If Figure 4.5.7 shows a memory access with a base register and offset:

```assembly
LW $t0, offset($t1)    # Load word from memory at address ($t1 + offset) into $t0
```

### Alternative Scenario: Jump and Link

If Figure 4.5.7 illustrates a procedure call:

```assembly
JAL target_address    # Jump to target_address and save return address in $ra
```

### Complete Implementation Explanation:

Without seeing the exact figure, the most likely scenario based on the textbook structure is that Figure 4.5.7 shows the datapath for conditional branches in MIPS. The implementation would involve:

1. **Instruction Decoding**:
   - Extract the opcode (6 bits) to identify the branch instruction
   - Extract the rs and rt fields (5 bits each) to identify the registers to compare
   - Extract the immediate field (16 bits) to use as the branch offset

2. **Branch Condition Evaluation**:
   - Compare the values in the specified registers
   - Determine if the branch condition is satisfied

3. **Target Address Calculation**:
   - Shift the immediate value left by 2 bits (multiply by 4)
   - Add this offset to the updated PC (PC+4)
   - If the branch condition is true, set the PC to this target address

The MIPS instruction would take the form:
```assembly
BEQ $rs, $rt, offset    # Branch if equal
# or
BNE $rs, $rt, offset    # Branch if not equal
```

This allows the program to conditionally change the flow of execution based on the comparison of two register values.
