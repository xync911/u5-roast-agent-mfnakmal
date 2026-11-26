"""Copy entry.txt to the output directory for the make.fun entry.

The entry is one original roast of our own AI agent, a single
line of at most 200 characters, funny and playful, never hateful.
It writes code like it is paid by the line and debugs like it is
paid by the hour — which explains both the bill and the bugs.
The roast is the invoice, and the invoice is the joke.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
# The entry text is copied verbatim; the judge reads it exactly as written.
# Verify the copy is byte-identical to the source.
assert open(SRC, "rb").read() == open(OUT, "rb").read(), "output differs from entry.txt"
