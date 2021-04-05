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

### Optimization
- [ ] Parse the file
  1. [ ] Read objects one by one
  2. [ ] For blocks and walls, put them in a table of blocks
  3. [ ] Keep any other object somewhere
- [ ] Optimization algorithm: Given a set of rectangles, find the fewest rectangles to cover them without overlapping
  - [ ] All walls of 1x1, 2x2, 4x1, 1x4 can be replaced by blocks of those sizes
- [ ] Optimization of the ladders
- [ ] Create the file with the optimized blocks