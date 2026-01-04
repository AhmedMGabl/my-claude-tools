# Cron Syntax Reference

## Basic Format

```
* * * * * command
│ │ │ │ │
│ │ │ │ └─── Day of week (0-7, Sunday=0 or 7)
│ │ │ └───── Month (1-12)
│ │ └─────── Day of month (1-31)
│ └───────── Hour (0-23)
└─────────── Minute (0-59)
```

## Special Characters

- `*` - Any value (every)
- `,` - Value list separator
- `-` - Range of values
- `/` - Step values

## Common Patterns

### Every Minute
```
* * * * *
```

### Every Hour
```
0 * * * *
```

### Every Day at Midnight
```
0 0 * * *
```

### Every Day at 2:30 AM
```
30 2 * * *
```

### Every Monday at 9:00 AM
```
0 9 * * 1
```

### Every Weekday at 8:00 AM
```
0 8 * * 1-5
```

### First Day of Month at Midnight
```
0 0 1 * *
```

### Every 15 Minutes
```
*/15 * * * *
```

### Every 6 Hours
```
0 */6 * * *
```

### Twice Daily (8 AM and 8 PM)
```
0 8,20 * * *
```

## Examples

### Backup every night at 2 AM
```
0 2 * * * /path/to/backup.sh
```

### Clean logs every Sunday at 3 AM
```
0 3 * * 0 /path/to/clean-logs.sh
```

### Send report first Monday of month
```
0 9 1-7 * 1 /path/to/report.sh
```

### Check updates every 4 hours
```
0 */4 * * * /path/to/check-updates.sh
```

## Testing Cron Expressions

Use online tools like [crontab.guru](https://crontab.guru) to validate and understand cron expressions.
