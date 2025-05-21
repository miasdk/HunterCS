# MIPS Assembly Language Crash Course

## Introduction

This crash course covers the essential MIPS assembly language concepts you need to understand for your computer architecture exam. While the exam focuses more on processor implementation than programming, a solid grasp of assembly fundamentals is crucial for comprehending how instructions execute on the hardware.

## 1. MIPS Register File

MIPS has 32 general-purpose 32-bit registers, referenced as `$0` through `$31` or by their conventional names:

| Register | Number | Usage | Preserved across calls? |
|----------|--------|-------|------------------------|
| `$zero`  | `$0`   | Constant 0 | N/A |
| `$at`    | `$1`   | Assembler temporary | No |
| `$v0-$v1`| `$2-$3`| Function return values | No |
| `$a0-$a3`| `$4-$7`| Function arguments | No |
| `$t0-$t7`| `$8-$15`| Temporary values | No |
| `$s0-$s7`| `$16-$23`| Saved values | Yes |
| `$t8-$t9`| `$24-$25`| More temporary values | No |
| `$k0-$k1`| `$26-$27`| Reserved for OS kernel | No |
| `$gp`    | `$28`  | Global pointer | Yes |
| `$sp`    | `$29`  | Stack pointer | Yes |
| `$fp`    | `$30`  | Frame pointer | Yes |
| `$ra`    | `$31`  | Return address | No |

Key points:
- `$zero` always contains the value 0 (hardware-enforced)
- `$sp` points to the top of the stack
- `$ra` stores the return address for function calls
- Temporary registers (`$t0-$t9`) can be overwritten by called functions
- Saved registers (`$s0-$s7`) must be preserved by called functions

## 2. Instruction Formats

MIPS has three basic instruction formats, each 32 bits wide:

### R-type (Register)
```
|  op   |  rs   |  rt   |  rd   | shamt |  funct |
| 6 bits| 5 bits| 5 bits| 5 bits| 5 bits| 6 bits |
```
- Used for register-to-register operations
- `op` = operation code (usually 0 for R-type)
- `rs`, `rt` = source registers
- `rd` = destination register
- `shamt` = shift amount (for shift instructions)
- `funct` = function code that specifies the exact operation

### I-type (Immediate)
```
|  op   |  rs   |  rt   |      immediate     |
| 6 bits| 5 bits| 5 bits|      16 bits       |
```
- Used for operations with immediate values or memory operations
- `op` = operation code
- `rs` = source register
- `rt` = destination register (or second source)
- `immediate` = 16-bit immediate value or address offset

### J-type (Jump)
```
|  op   |          address             |
| 6 bits|          26 bits             |
```
- Used for jump instructions
- `op` = operation code
- `address` = target address (shifted left 2 bits and combined with high-order PC bits)

## 3. Basic Instructions

### Data Movement
```
lw   $rt, offset($rs)    # Load word: $rt = Memory[$rs + offset]
sw   $rt, offset($rs)    # Store word: Memory[$rs + offset] = $rt
li   $rd, immediate      # Load immediate: $rd = immediate
move $rd, $rs            # Move: $rd = $rs
mfhi $rd                 # Move from HI: $rd = HI
mflo $rd                 # Move from LO: $rd = LO
```

### Arithmetic
```
add  $rd, $rs, $rt       # Add: $rd = $rs + $rt
addi $rt, $rs, imm       # Add immediate: $rt = $rs + imm
sub  $rd, $rs, $rt       # Subtract: $rd = $rs - $rt
mult $rs, $rt            # Multiply: HI:LO = $rs * $rt
div  $rs, $rt            # Divide: LO = $rs / $rt, HI = $rs % $rt
```

### Logical
```
and  $rd, $rs, $rt       # Bitwise AND: $rd = $rs & $rt
andi $rt, $rs, imm       # Bitwise AND immediate: $rt = $rs & imm
or   $rd, $rs, $rt       # Bitwise OR: $rd = $rs | $rt
ori  $rt, $rs, imm       # Bitwise OR immediate: $rt = $rs | imm
xor  $rd, $rs, $rt       # Bitwise XOR: $rd = $rs ^ $rt
xori $rt, $rs, imm       # Bitwise XOR immediate: $rt = $rs ^ imm
nor  $rd, $rs, $rt       # Bitwise NOR: $rd = ~($rs | $rt)
```

### Shifts
```
sll  $rd, $rt, shamt     # Shift left logical: $rd = $rt << shamt
srl  $rd, $rt, shamt     # Shift right logical: $rd = $rt >> shamt
sra  $rd, $rt, shamt     # Shift right arithmetic: $rd = $rt >> shamt (sign-extended)
sllv $rd, $rt, $rs       # Shift left logical variable: $rd = $rt << $rs
srlv $rd, $rt, $rs       # Shift right logical variable: $rd = $rt >> $rs
```

### Comparisons
```
slt  $rd, $rs, $rt       # Set less than: $rd = ($rs < $rt) ? 1 : 0
slti $rt, $rs, imm       # Set less than immediate: $rt = ($rs < imm) ? 1 : 0
sltu $rd, $rs, $rt       # Set less than unsigned: $rd = ($rs < $rt) ? 1 : 0 (unsigned)
```

### Branches and Jumps
```
beq  $rs, $rt, label     # Branch if equal: if ($rs == $rt) goto label
bne  $rs, $rt, label     # Branch if not equal: if ($rs != $rt) goto label
j    label               # Jump: goto label
jal  label               # Jump and link: $ra = PC + 4; goto label
jr   $rs                 # Jump register: goto address in $rs
```

## 4. Addressing Modes

MIPS supports several addressing modes:

### 1. Register Addressing
Operand is in a register:
```
add $t0, $t1, $t2        # $t0 = $t1 + $t2
```

### 2. Immediate Addressing
Operand is a constant in the instruction:
```
addi $t0, $t1, 100       # $t0 = $t1 + 100
```

### 3. Base Addressing (for memory)
Operand is in memory, address calculated as base register + offset:
```
lw $t0, 4($sp)           # $t0 = Memory[$sp + 4]
sw $t0, -8($s0)          # Memory[$s0 - 8] = $t0
```

### 4. PC-relative Addressing (for branches)
Target address calculated as PC + 4 + (offset × 4):
```
beq $t0, $zero, loop     # if ($t0 == 0) goto loop
```

### 5. Pseudo-direct Addressing (for jumps)
Target address formed from high-order bits of PC and jump target from instruction:
```
j exit                   # goto exit
```

## 5. Memory and Stack Operations

### Stack Operations
The stack grows downward in memory (from high to low addresses):
```
# Push onto stack
addi $sp, $sp, -4        # Decrement stack pointer
sw   $t0, 0($sp)         # Store value on stack

# Pop from stack
lw   $t0, 0($sp)         # Load value from stack
addi $sp, $sp, 4         # Increment stack pointer
```

### Procedure Call Example
```
# Caller prepares to call function
addi $sp, $sp, -8        # Make space on stack
sw   $ra, 4($sp)         # Save return address
sw   $s0, 0($sp)         # Save $s0 (callee-saved)
jal  function            # Call function
lw   $s0, 0($sp)         # Restore $s0
lw   $ra, 4($sp)         # Restore return address
addi $sp, $sp, 8         # Restore stack pointer
jr   $ra                 # Return to caller

# Callee function
function:
    # Function body
    jr $ra                # Return to caller
```

## 6. Common Programming Patterns

### Conditional Statements
```
# if (a < b) max = b; else max = a;
    slt  $t0, $a0, $a1    # $t0 = 1 if $a0 < $a1
    beq  $t0, $zero, else # branch to else if $a0 >= $a1
    move $v0, $a1         # max = b
    j    endif
else:
    move $v0, $a0         # max = a
endif:
```

### Loops
```
# for (i = 0; i < 10; i++) sum += array[i];
    li   $t0, 0           # i = 0
    li   $t1, 0           # sum = 0
    li   $t2, 10          # loop bound
loop:
    beq  $t0, $t2, done   # exit loop if i == 10
    sll  $t3, $t0, 2      # $t3 = i * 4 (byte offset)
    add  $t3, $t3, $a0    # $t3 = address of array[i]
    lw   $t4, 0($t3)      # $t4 = array[i]
    add  $t1, $t1, $t4    # sum += array[i]
    addi $t0, $t0, 1      # i++
    j    loop
done:
    move $v0, $t1         # return sum
```

## 7. Important Concepts for Computer Architecture

### Instruction Execution Cycle
For single-cycle MIPS:
1. **Fetch**: Read instruction from memory at PC address
2. **Decode**: Identify instruction type and operands
3. **Execute**: Perform ALU operation or address calculation
4. **Memory**: Access memory for load/store
5. **Write-back**: Write result to register file

### MIPS Instruction Encoding Examples

**add $t0, $t1, $t2**
- R-type: op=0, rs=$t1, rt=$t2, rd=$t0, shamt=0, funct=32
- Binary: 000000 01001 01010 01000 00000 100000
- Hex: 0x01284020

**lw $t0, 8($s0)**
- I-type: op=35, rs=$s0, rt=$t0, immediate=8
- Binary: 100011 10000 01000 0000000000001000
- Hex: 0x8E080008

**beq $t0, $zero, offset**
- I-type: op=4, rs=$t0, rt=$zero, immediate=offset
- Binary: 000100 01000 00000 (16-bit offset)
- Hex: 0x11000xxx (where xxx is the encoded offset)

### Memory Alignment
- MIPS requires word alignment (addresses must be multiples of 4)
- Accessing unaligned addresses causes exceptions
- This simplifies processor implementation

### Delayed Branches
- In pipelined MIPS, the instruction after a branch is always executed (branch delay slot)
- Compiler/programmer can optimize by reordering instructions
- This simplifies pipeline control

## 8. Example: Connecting Assembly to Processor Implementation

### Instruction: add $t0, $t1, $t2

**Execution on Single-Cycle MIPS**:
1. **Fetch**: PC → IM → Instruction Register
2. **Decode**: 
   - Control Unit recognizes R-type (opcode=0)
   - Register File reads $t1 and $t2
3. **Execute**: ALU performs addition
4. **Memory**: No memory access
5. **Write-back**: ALU result written to $t0

**Control Signals**:
- RegDst = 1 (use rd field for destination)
- ALUSrc = 0 (use rt for ALU input)
- MemtoReg = 0 (use ALU result)
- RegWrite = 1 (write to register)
- MemRead = 0 (no memory read)
- MemWrite = 0 (no memory write)
- Branch = 0 (not a branch)
- ALUOp = 10 (R-type ALU operation)

### Instruction: lw $t0, 4($s0)

**Execution on Single-Cycle MIPS**:
1. **Fetch**: PC → IM → Instruction Register
2. **Decode**: 
   - Control Unit recognizes lw (opcode=35)
   - Register File reads $s0
3. **Execute**: ALU calculates $s0 + 4
4. **Memory**: Data memory reads from calculated address
5. **Write-back**: Memory data written to $t0

**Control Signals**:
- RegDst = 0 (use rt field for destination)
- ALUSrc = 1 (use immediate for ALU input)
- MemtoReg = 1 (use memory data)
- RegWrite = 1 (write to register)
- MemRead = 1 (read from memory)
- MemWrite = 0 (no memory write)
- Branch = 0 (not a branch)
- ALUOp = 00 (address calculation)

## 9. Key Takeaways for the Exam

1. **Understand instruction formats** and how they map to machine code
2. **Know the datapath** for different instruction types (R-type, lw, sw, beq, j)
3. **Recognize control signal patterns** for different instructions
4. **Identify pipeline hazards** in assembly code sequences
5. **Understand how branch prediction** affects code with loops and conditionals
6. **Recognize memory access patterns** and their performance implications
7. **Connect assembly code** to hardware operations in the processor

Remember, for your computer architecture exam, you don't need to be an expert MIPS programmer, but you do need to understand how assembly instructions translate to hardware operations and control signals.
