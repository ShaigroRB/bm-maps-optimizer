export class BlocksTable {
  type: string;
  sound: string;
  table: number[][];

  constructor(type: string, sound: string, table: number[][] | null = null) {
    this.type = type;
    this.sound = sound;
    this.table = table ? [...table] : [];
  }

  get(item: number): number[] {
    return this.table[item];
  }

  set(key: number, value: number[]): void {
    this.table[key] = value;
  }

  toString(): string {
    return `Type: ${this.type}\n Sound: ${this.sound}\n Table: ${JSON.stringify(
      this.table
    )}\n`;
  }
}
