import { copyFileSync, existsSync, mkdirSync, readFileSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const src = join(here, "entry.png");
const outDir = process.env.MAKEFUN_OUTPUT_DIR || "/output";
const out = join(outDir, "entry.png");

if (!existsSync(src)) {
  throw new Error(`entry image missing next to main.ts: ${src}`);
}
mkdirSync(outDir, { recursive: true });
copyFileSync(src, out);

const buf = readFileSync(out);
if (buf.length < 8 || buf[0] !== 0x89 || buf[1] !== 0x50 || buf[2] !== 0x4e || buf[3] !== 0x47) {
  throw new Error("output is not a PNG");
}
const width = buf.readUInt32BE(16);
const height = buf.readUInt32BE(20);
if (width > 1024 || height > 1024) {
  throw new Error(`image too large: ${width}x${height}`);
}
if (statSync(out).size > 1048576) {
  throw new Error("image over 1 MiB");
}
console.log(`wrote ${out} (${width}x${height}, ${buf.length} bytes)`);
