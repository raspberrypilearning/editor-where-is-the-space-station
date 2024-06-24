<h2 class="c-project-heading--task">Store latitude and longitude</h2>
--- task ---
➡️ Store the current latitude and longitude of the ISS.
--- /task --- 

Latitude and longitude are used to give coordinates to locations on the Earth’s surface.

Create two variables and use them to store the **latitude** and **longitude** from the data you have just received. 

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 10
---

latitude = data['latitude']
longitude = data['longitude']
print(f"Latitude:{latitude}, Longitude:{longitude}")

--- /code ---
</div>

**Test:** Run your code and you should see the values of latitude and longitude printed.

<div class="c-project-callout c-project-callout--tip">

### Tip
You can delete the line `print(data)` if you like.
</div>


