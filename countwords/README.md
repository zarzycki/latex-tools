Code to take a TeX folder of the AMS LaTeX template and convert to word count. The code compiles the AMS TeX file into HTML using an updated `cls` file that doesn't print things AMS doesn't count (bibliography, etc.). It also modifies a TeX file to delete certain things not counted such as significance statements and also forces figures and tables to not be printed.

## Instructions:

```
mamba create -n wordcount -c conda-forge selenium bs4
conda activate wordcount
```

1. Download *.zip file from Overleaf. Unzip and call the new folder `$TEXDIR`.
2. Create environment that includes bs4 and selenium (see above).
3. Copy all files from this repo into `$TEXDIR`.
4. Go into `$TEXDIR` and `chmod +x ./auto.sh`
5. Run `./auto.sh $FILEBASE` from `$TEXDIR` where `$FILEBASE` is the name of the template file *without* the *.tex extension. Ex: `$> ./auto.sh template` if your TeX file is named `template.tex`.

Should eventually give:

```
Rendered Word Count: 8274
```

NOTE: AMS reported 8324 words for this particular test, likely copying into Word. Some potential failure modes:

1. htlatex converts LaTeX equations to images so equations/variables/etc. are counted as words?