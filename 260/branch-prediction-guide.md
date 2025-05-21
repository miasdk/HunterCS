# CSCI 260: Comprehensive Branch Prediction Guide

## Table of Contents
1. [Introduction to Branch Prediction](#introduction-to-branch-prediction)
2. [Branch Prediction Strategies](#branch-prediction-strategies)
   - [Static Prediction](#static-prediction)
   - [Dynamic Prediction](#dynamic-prediction)
   - [State Diagram for 2-bit Predictor](#state-diagram-for-2-bit-predictor)
3. [Detailed Solution to Problem 4.29](#detailed-solution-to-problem-429)
   - [Part 1: Always-Taken and Always-Not-Taken Predictors](#part-1-always-taken-and-always-not-taken-predictors)
   - [Part 2: 2-bit Predictor for First Four Branches](#part-2-2-bit-predictor-for-first-four-branches)
   - [Part 3: Long-term 2-bit Predictor Accuracy](#part-3-long-term-2-bit-predictor-accuracy)
   - [Key Observations](#key-observations)
4. [Calculating Performance Impact of Branch Prediction](#calculating-performance-impact-of-branch-prediction)
5. [Branch Prediction in Modern Processors](#branch-prediction-in-modern-processors)

## Introduction to Branch Prediction

Branch prediction is a crucial technique in modern processor design that attempts to guess the outcome of a branch instruction before its execution is complete. It's essential for maintaining the efficiency of pipelined processors.

Without branch prediction, pipelines would need to stall when encountering a branch instruction until the branch condition is evaluated, resulting in significant performance degradation.

## Branch Prediction Strategies

### Static Prediction

Static prediction uses fixed rules that don't change based on the program's execution history.

#### Always-Not-Taken Strategy
- **Mechanism**: Always predict branches will not be taken
- **Implementation**: Continue fetching instructions sequentially
- **Advantages**: Simple to implement
- **Disadvantages**: Performs poorly for loops and backwards branches

#### Always-Taken Strategy
- **Mechanism**: Always predict branches will be taken
- **Implementation**: Start fetching from the branch target immediately
- **Advantages**: Works well for loops (backward branches)
- **Disadvantages**: Poor performance for forward branches

#### Based on Branch Direction
- **Mechanism**: Backward branches (negative displacement) predicted taken; forward branches (positive displacement) predicted not taken
- **Implementation**: Use the sign bit of the branch offset
- **Advantages**: Better accuracy than single-strategy approaches
- **Disadvantages**: Still doesn't adapt to actual program behavior

### Dynamic Prediction

Dynamic prediction uses information from the program's execution history to make predictions.

#### 1-bit Predictor
- **Mechanism**: Remember the last outcome of each branch
- **Implementation**: Use a 1-bit field for each branch (typically in a branch history table)
- **Advantages**: Simple, adapts to program behavior
- **Disadvantages**: Performs poorly for loops (mispredicts twice per loop)

#### 2-bit Saturating Counter Predictor
- **Mechanism**: Use a 2-bit counter per branch with hysteresis
- **Implementation**: Four states that require two consecutive mispredictions to change direction
- **Advantages**: Works well for loops, resilient to occasional deviations
- **Disadvantages**: More complex, slower adaptation to changing patterns

#### Correlating Predictors
- **Mechanism**: Consider outcomes of multiple previous branches
- **Implementation**: Global history register + pattern history table
- **Advantages**: Can detect patterns across different branches
- **Disadvantages**: More complex, higher hardware overhead

#### Tournament Predictors
- **Mechanism**: Use multiple predictors simultaneously
- **Implementation**: Meta-predictor chooses which predictor to trust
- **Advantages**: Combines benefits of different prediction strategies
- **Disadvantages**: Most complex, highest hardware overhead

### State Diagram for 2-bit Predictor

The 2-bit saturating counter predictor uses four states:
- **Strongly Not Taken (00)**: Predict not taken, stay in this state if correct, move to Weakly Not Taken if wrong
- **Weakly Not Taken (01)**: Predict not taken, move to Strongly Not Taken if correct, move to Weakly Taken if wrong
- **Weakly Taken (10)**: Predict taken, move to Strongly Taken if correct, move to Weakly Not Taken if wrong
- **Strongly Taken (11)**: Predict taken, stay in this state if correct, move to Weakly Taken if wrong

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

## Detailed Solution to Problem 4.29

**Problem Statement**: Examine the accuracy of various branch predictors for the following repeating pattern (in a loop) of branch outcomes: T, NT, T, T, NT. (Where T = Taken, NT = Not Taken)

### Part 1: Always-Taken and Always-Not-Taken Predictors

For this pattern (T, NT, T, T, NT), let's analyze the performance of the static predictors:

#### Always-Taken Predictor:
- **Predictions**: T, T, T, T, T
- **Actual outcomes**: T, NT, T, T, NT
- **Comparison**: ✓, ✗, ✓, ✓, ✗
- **Correct predictions**: 3 out of 5
- **Accuracy**: 3/5 = 60%

#### Always-Not-Taken Predictor:
- **Predictions**: NT, NT, NT, NT, NT
- **Actual outcomes**: T, NT, T, T, NT
- **Comparison**: ✗, ✓, ✗, ✗, ✓
- **Correct predictions**: 2 out of 5
- **Accuracy**: 2/5 = 40%

### Part 2: 2-bit Predictor for First Four Branches

Now let's analyze how a 2-bit predictor performs for the first four branches, assuming it starts in the Strongly Not Taken (00) state:

**Initial state: Strongly Not Taken (00)**

1. **Branch 1**:
   - **Prediction**: NT (we're in Strongly Not Taken)
   - **Actual outcome**: T
   - **Result**: Misprediction
   - **State transition**: 00 → 01 (Strongly Not Taken → Weakly Not Taken)

2. **Branch 2**:
   - **Prediction**: NT (we're in Weakly Not Taken)
   - **Actual outcome**: NT
   - **Result**: Correct prediction
   - **State transition**: 01 → 00 (Weakly Not Taken → Strongly Not Taken)

3. **Branch 3**:
   - **Prediction**: NT (we're in Strongly Not Taken)
   - **Actual outcome**: T
   - **Result**: Misprediction
   - **State transition**: 00 → 01 (Strongly Not Taken → Weakly Not Taken)

4. **Branch 4**:
   - **Prediction**: NT (we're in Weakly Not Taken)
   - **Actual outcome**: T
   - **Result**: Misprediction
   - **State transition**: 01 → 10 (Weakly Not Taken → Weakly Taken)

For the first four branches, the 2-bit predictor made 1 correct prediction and 3 mispredictions.
**Accuracy for first four branches**: 1/4 = 25%

### Part 3: Long-term 2-bit Predictor Accuracy

To find the long-term accuracy, we need to continue tracing until we find a stable pattern. Let's pick up where we left off:

5. **Branch 5**:
   - **Prediction**: T (we're in Weakly Taken)
   - **Actual outcome**: NT
   - **Result**: Misprediction
   - **State transition**: 10 → 01 (Weakly Taken → Weakly Not Taken)

Let's continue through another iteration of the pattern:

6. **Branch 6** (repeat of Branch 1):
   - **Prediction**: NT (we're in Weakly Not Taken)
   - **Actual outcome**: T
   - **Result**: Misprediction
   - **State transition**: 01 → 10 (Weakly Not Taken → Weakly Taken)

7. **Branch 7** (repeat of Branch 2):
   - **Prediction**: T (we're in Weakly Taken)
   - **Actual outcome**: NT
   - **Result**: Misprediction
   - **State transition**: 10 → 01 (Weakly Taken → Weakly Not Taken)

8. **Branch 8** (repeat of Branch 3):
   - **Prediction**: NT (we're in Weakly Not Taken)
   - **Actual outcome**: T
   - **Result**: Misprediction
   - **State transition**: 01 → 10 (Weakly Not Taken → Weakly Taken)

9. **Branch 9** (repeat of Branch 4):
   - **Prediction**: T (we're in Weakly Taken)
   - **Actual outcome**: T
   - **Result**: Correct prediction
   - **State transition**: 10 → 11 (Weakly Taken → Strongly Taken)

10. **Branch 10** (repeat of Branch 5):
    - **Prediction**: T (we're in Strongly Taken)
    - **Actual outcome**: NT
    - **Result**: Misprediction
    - **State transition**: 11 → 10 (Strongly Taken → Weakly Taken)

Let's continue one more iteration to confirm the pattern:

11. **Branch 11** (repeat of Branch 1):
    - **Prediction**: T (we're in Weakly Taken)
    - **Actual outcome**: T
    - **Result**: Correct prediction
    - **State transition**: 10 → 11 (Weakly Taken → Strongly Taken)

12. **Branch 12** (repeat of Branch 2):
    - **Prediction**: T (we're in Strongly Taken)
    - **Actual outcome**: NT
    - **Result**: Misprediction
    - **State transition**: 11 → 10 (Strongly Taken → Weakly Taken)

13. **Branch 13** (repeat of Branch 3):
    - **Prediction**: T (we're in Weakly Taken)
    - **Actual outcome**: T
    - **Result**: Correct prediction
    - **State transition**: 10 → 11 (Weakly Taken → Strongly Taken)

14. **Branch 14** (repeat of Branch 4):
    - **Prediction**: T (we're in Strongly Taken)
    - **Actual outcome**: T
    - **Result**: Correct prediction
    - **State transition**: 11 → 11 (Strongly Taken → Strongly Taken)

15. **Branch 15** (repeat of Branch 5):
    - **Prediction**: T (we're in Strongly Taken)
    - **Actual outcome**: NT
    - **Result**: Misprediction
    - **State transition**: 11 → 10 (Strongly Taken → Weakly Taken)

Examining the state after Branch 15, we see it matches the state after Branch 10 (Weakly Taken). This indicates we've reached a stable cycle.

In this stable cycle (branches 11-15), we have:
- **Correct predictions**: 3 (branches 11, 13, 14)
- **Mispredictions**: 2 (branches 12, 15)
- **Long-term accuracy**: 3/5 = 60%

To verify, let's check if branches 16-20 follow the same pattern as branches 11-15:
- Branch 16 (state = Weakly Taken): Predict T, Actual T → Correct
- Branch 17 (state = Strongly Taken): Predict T, Actual NT → Wrong
- Branch 18 (state = Weakly Taken): Predict T, Actual T → Correct
- Branch 19 (state = Strongly Taken): Predict T, Actual T → Correct
- Branch 20 (state = Strongly Taken): Predict T, Actual NT → Wrong

This confirms our long-term accuracy of 60%.

### Key Observations

1. **Static vs. Dynamic Prediction**:
   - Always-Taken predictor: 60% accuracy
   - Always-Not-Taken predictor: 40% accuracy
   - 2-bit predictor (long-term): 60% accuracy

2. **Adaptation Period**:
   - The 2-bit predictor performs poorly initially (25%)
   - It takes several iterations to reach its stable behavior
   - After adaptation, it matches the always-taken predictor

3. **State Oscillation**:
   - The 2-bit predictor eventually oscillates between Weakly Taken (10), Strongly Taken (11), and back
   - This pattern aligns well with predicting 3 out of 5 branches correctly

4. **Pattern-Dependent Performance**:
   - For this specific pattern, the 2-bit predictor doesn't outperform the simpler always-taken predictor
   - This demonstrates that predictor effectiveness depends on the branch pattern

5. **Hysteresis Benefit**:
   - The 2-bit predictor's hysteresis helps it maintain the "taken" prediction for most of the pattern
   - This is why it ends up matching the always-taken predictor's performance

## Calculating Performance Impact of Branch Prediction

### Performance Impact Formula

The impact of branch prediction on pipeline performance can be calculated as:

**CPI Impact = Branch Frequency × Misprediction Rate × Misprediction Penalty**

Where:
- **Branch Frequency**: Percentage of instructions that are branches
- **Misprediction Rate**: Percentage of branches that are incorrectly predicted
- **Misprediction Penalty**: Additional cycles required due to a misprediction

### Example Calculation

For a processor with:
- Branch frequency = 15% (15% of all instructions are branches)
- Branch prediction accuracy = 90% (misprediction rate = 10%)
- Misprediction penalty = 3 cycles (typical for a 5-stage pipeline)

**CPI Impact = 0.15 × 0.10 × 3 = 0.045**

If the ideal CPI is 1, the effective CPI becomes 1.045, representing a 4.5% reduction in performance due to branch mispredictions.

### Problem from Homework

**Problem Statement**: Suppose that mispredictions need a 4-cycle stall, the branch prediction algorithm has an accuracy of 95%, and 1/7 of all instructions are branches. Assume you are running the MIPS pipelined architecture at 2 GHz, with all data hazards handled by forwarding. What is the throughput of the resulting processor?

**Solution**:

1. Calculate the CPI impact:
   - Branch frequency = 1/7 ≈ 0.143 (14.3%)
   - Misprediction rate = 0.05 (5%)
   - Misprediction penalty = 4 cycles
   - **CPI Impact = 0.143 × 0.05 × 4 = 0.0286**

2. Calculate the effective CPI:
   - Ideal CPI = 1
   - Effective CPI = 1 + 0.0286 = 1.0286

3. Calculate the throughput:
   - Clock rate = 2 GHz = 2 × 10^9 Hz
   - Throughput = Clock rate / Effective CPI
   - Throughput = (2 × 10^9) / 1.0286 ≈ 1.944 × 10^9 instructions/second
   - **Throughput = 1.944 BIPS** (Billion Instructions Per Second)

## Branch Prediction in Modern Processors

Modern processors employ sophisticated branch prediction strategies:

1. **Multi-level Predictors**: Combine local and global history for better accuracy

2. **Neural Branch Predictors**: Use perceptron-based or neural network approaches

3. **Loop Detectors**: Specialized hardware to identify and predict loops with specific iteration counts

4. **Indirect Branch Predictors**: Target special handling for indirect jumps and virtual function calls

5. **Return Address Stack**: Specialized hardware for predicting return addresses from function calls

The importance of branch prediction has grown with deeper pipelines, as misprediction penalties have increased. A misprediction in a modern processor with 15-20 pipeline stages can waste significantly more cycles than in a simpler 5-stage pipeline.
