<h1 align="center">
    <img src="./assets/horizontal_icon_128x128.png" />
</h1>

# Boring Man Maps Optimizer
Tool to optimize maps from the game Boring Man - OTSC.

## Why?
Because people are too lazy to optimize maps manually (*me included*) and they generally don't use the wall tool right from the start.

## Todo
### UI
- [ ] File picker
- [ ] Path where to save the resulting file
- [ ] Start optimization button
- [ ] Progress bar with some infos
- [ ] Options
  - [ ] Optimize blocks
  - [ ] Optimize ladders

### Parsing, Optimization & Creation of the new map
- [x] Parse the file
  1. [x] Read objects one by one
  2. x ] For blocks and walls, put them in a table of blocks
     1. [x] Handle simple blocks (no type, no ambience)
     2. [x] Handle block types
     3. [x] Handle block ambiences
  3. [x] Keep any other object somewhere
  4. [x] Create a table from a list of blocks
- [ ] Optimization algorithm: Given a set of rectangles, find the fewest rectangles to cover them without overlapping
  - [ ] All walls of 1x1, 2x2, 4x1, 1x4 can be replaced by blocks of those sizes
- [ ] Optimization of the ladders
- [ ] Create a new file with the optimized blocks

## How to run this project?
1. Download the project
2. `cd bm-map-optimizer/`
3. `python -m venv new_env`
4. `python -m pip install -e .`
5. `python -m bmmo.main bmap.txt`