# Modding

In order to mod Rev 3, you'll likely want to extract and rebuild using
[Wiimms ISO Tool](https://wit.wiimm.de/). Once downloaded, extract the files from
`rev3.iso` to the folder `rev3` with:

```bash
wit extract rev3.iso rev3/
```

After done modifying the files, create a new ISO with:

```bash
wit copy rev3/ rev3_new.iso
```
