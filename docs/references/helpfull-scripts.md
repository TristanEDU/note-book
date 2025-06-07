#Usefull Scripts

A usfull set of scripts for your projects

##Element outline script
Simply set the `document.querySelectorAll` to the outermost element and everything inside of it will be outlined
```
<script>
      window.addEventListener("DOMContentLoaded", () => {
        const colors = [
          "red",
          "blue",
          "green",
          "orange",
          "purple",
          "cyan",
          "magenta",
        ];
        document.querySelectorAll("#whyFrontSection *").forEach((el, i) => {
          el.style.outline = `1px solid ${colors[i % colors.length]}`;
        });
      });
    </script>
```
