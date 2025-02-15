export class Block {
  x: number;
  y: number;
  width: number;
  height: number;
  type: string;
  sound: string;

  constructor(
    x: number,
    y: number,
    width: number,
    height: number,
    type: string,
    sound: string
  ) {
    this.x = x;
    this.y = y;
    this.width = width;
    this.height = height;
    this.type = type;
    this.sound = sound;
  }
}
