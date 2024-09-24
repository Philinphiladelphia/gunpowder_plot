**Option 1: Simple Fire Burst**

```json
{
  "name": "Fire Burst",
  "max_size": 10,
  "elements": ["fire"],
  "lines": [
    {
      "start": [5, -5],
      "end": [5, 5],
      "width": 2,
      "velocity_x": 75,
      "velocity_y": 50
    },
    {
      "start": [-5, 5],
      "end": [5, 5],
      "width": 2,
      "velocity_x": -75,
      "velocity_y": 50
    }
  ]
}
```

**Option 2: Spiral Fire Burst**

```json
{
  "name": "Spiral Fire Burst",
  "max_size": 10,
  "elements": ["fire"],
  "lines": [
    {
      "start": [0, -5],
      "end": [0, 5],
      "width": 2,
      "velocity_x": 50,
      "velocity_y": 75
    },
    {
      "start": [-5, 0],
      "end": [5, 0],
      "width": 1.5,
      "velocity_x": 50,
      "velocity_y": -75
    }
  ]
}
```

**Option 3: Exploding Fire Burst**

```json
{
  "name": "Exploding Fire Burst",
  "max_size": 10,
  "elements": ["fire"],
  "lines": [
    {
      "start": [0, -5],
      "end": [0, 5],
      "width": 3,
      "velocity_x": 75,
      "velocity_y": 50
    },
    {
      "start": [-2.5, 0],
      "end": [2.5, 0],
      "width": 1,
      "velocity_x": -100,
      "velocity_y": 25
    }
  ]
}
```