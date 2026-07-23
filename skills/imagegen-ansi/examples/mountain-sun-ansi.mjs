import { realpathSync } from "node:fs";
import { pathToFileURL } from "node:url";

const BITMAP = [
  "                   ##########",
  "                #####      #####",
  "              ###              ###",
  "            ###                  ###",
  "          ###                      ###",
  "         ###                        ###",
  "        ##                            ##",
  "       ##                              ##",
  "      ###           ########           ###",
  "     ###          ############          ###",
  "    ###         ################         ###",
  "    ##         ##################         ##",
  "   ###        ####################         ##",
  "   ##        ######################        ##",
  "  ##        ########################        ##",
  "  ##        ########################        ##",
  " ##        ##########################        ##",
  " ##        ##########################        ##",
  " #        ############################        #",
  "##        ############################        ##",
  "##        ############################        ##",
  "#         ############################         #",
  "#         ########  ##################         #",
  "#         ####### ## #################         #",
  "#         ###### #### ################         #",
  "#         ##### ###### ######### ####          #",
  "#          ### ######## #######   ###          #",
  "#          ## ########## ##### ##  ##          #",
  "#            ############ ### ####             #",
  "##          ############## # ######           ##",
  "##         ################  #######          ##",
  " #        ################## ########         #",
  " ##      #################### ########       ##",
  " ##      ##################### ########      ##",
  "  ##    ####################### ########    ##",
  "  ##   ######################### ########   ##",
  "   ## ########################### ######## ##",
  "   ############################### ##########",
  "    ############################### ########",
  "    ########################################",
  "     ######################################",
  "      ####################################",
  "       ##################################",
  "        ################################",
  "         ##############################",
  "          ############################",
  "            ########################",
  "             #####################",
  "                ################",
  "                   ##########"
];
const SOURCE_WIDTH = Math.max(...BITMAP.map((row) => row.length));

export function renderAnsiArt(
  terminalWidth = SOURCE_WIDTH + 4,
  color = process.stdout.isTTY === true && process.env.NO_COLOR === undefined,
) {
  const width = Math.min(SOURCE_WIDTH, Math.max(1, terminalWidth - 4));
  let height = Math.max(2, Math.round((width * BITMAP.length) / SOURCE_WIDTH));
  height += height % 2;

  const isSet = (x, y) => {
    const sourceX = Math.floor((x * SOURCE_WIDTH) / width);
    const sourceY = Math.floor((y * BITMAP.length) / height);
    return BITMAP[sourceY]?.[sourceX] === "#";
  };

  const margin = " ".repeat(Math.max(0, Math.floor((terminalWidth - width) / 2)));
  const lines = [];
  for (let y = 0; y < height; y += 2) {
    let line = "";
    for (let x = 0; x < width; x += 1) {
      const top = isSet(x, y);
      const bottom = isSet(x, y + 1);
      line += top ? (bottom ? "█" : "▀") : bottom ? "▄" : " ";
    }
    lines.push(margin + line.trimEnd());
  }

  const art = lines.join("\n");
  return color ? `\u001b[97m${art}\u001b[0m` : art;
}

if (
  process.argv[1] &&
  import.meta.url === pathToFileURL(realpathSync(process.argv[1])).href
) {
  process.stdout.write(`${renderAnsiArt(process.stdout.columns)}\n`);
}
