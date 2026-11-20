// A working news-image-daily entry (Node 22, standard library only): its image is the entry.png beside this file, and
// the program copies it to /output/entry.png. A starting point, not a winner: replace the image. The gate takes a
// whole PNG or JPEG of at most 1 MiB and 1024 by 1024 pixels, and the judge sees exactly the bytes copied.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { createHash } from 'node:crypto';
import { copyFileSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

copyFileSync(new URL('./entry.png', import.meta.url), join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png'));

// Verify the copy landed byte-for-byte: hash the source and the output and refuse to
// report success if they differ, so a truncated or partial write can never pass silently.
const entryDate = '2026-11-20';
const outputPath = join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png');
const hashFile = (target) => createHash('sha256').update(readFileSync(target)).digest('hex');
const sourceDigest = hashFile(new URL('./entry.png', import.meta.url));
const outputDigest = hashFile(outputPath);
if (sourceDigest !== outputDigest) {
  throw new Error(`news-image-20261120 copy mismatch: source ${sourceDigest} != output ${outputDigest}`);
}
console.log(`news-image-20261120 (${entryDate}): entry.png copied and verified sha256 ${sourceDigest.slice(0, 16)}`);
