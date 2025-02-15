export const COLOR_TYPE_NORMAL = "#808080";
export const COLOR_TYPE_HEAL = "#00ff00";
export const COLOR_TYPE_AMMO = "#ffff00";
export const COLOR_TYPE_DMG = "#ffa040";
export const COLOR_TYPE_DEATH = "#ff0000";
export const COLOR_TYPE_BOUNCY = "#ff00ff";
export const COLOR_TYPE_ICY = "#008080";
export const COLOR_TYPE_NOWEAP = "#000080";
export const COLOR_TYPE_POISON = "#9f31c6";
export const COLOR_TYPE_BURN = "#ff6200";

export const COLORS_PER_TYPE: Record<string, string> = {
  "0": COLOR_TYPE_NORMAL,
  "1": COLOR_TYPE_HEAL,
  "2": COLOR_TYPE_AMMO,
  "3": COLOR_TYPE_DMG,
  "4": COLOR_TYPE_DEATH,
  "5": COLOR_TYPE_BOUNCY,
  "6": COLOR_TYPE_ICY,
  "7": COLOR_TYPE_NOWEAP,
  "8": "#ffffff", // there is no type 8 in the game
  "9": COLOR_TYPE_POISON,
  "10": COLOR_TYPE_BURN,
};
