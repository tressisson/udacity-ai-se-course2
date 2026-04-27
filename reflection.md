Project Reflection - Personal Finance Manager


Singleton Pattern (Balance)

I used the Singleton pattern for the Balance class because the whole point of a balance manager is that there should be exactly one source of truth for how much money is in the account. If two different parts of the app created their own Balance objects they'd quickly get out of sync and you'd end up with inconsistent data. By overriding __new__, I make sure every call to Balance() returns the same instance.

The tricky part was testing. The singleton persists between test cases, so I added a _reset() classmethod to wipe the instance before each test. It felt a little hacky but it worked. In a real production app I'd probably just pass the balance around using dependency injection instead of relying on a global singleton, but for this project it made sense.


Adapter Pattern (TransactionAdapter)

The Adapter pattern made sense here because the assignment described an external freelance platform that gives you invoices with fields like invoice_id, project_name, and amount_due, none of which match what the rest of the app expects. Rather than changing either the external class or the core Transaction class, I created TransactionAdapter to sit in between and translate one into the other.

This felt like a realistic scenario. In real projects you almost always end up dealing with third-party APIs or older systems that use different data formats, and the Adapter pattern is a clean way to handle that without making a mess of your core code. The one downside is that if you had a lot of different external sources you'd end up with a lot of small adapter files, but for this project that wasn't an issue.


Observer Pattern (LowBalanceAlertObserver and PrintBalanceObserver)

I used the Observer pattern so that the Balance class doesn't have to know anything about what should happen after a transaction is applied. All it does is loop through its list of observers and call update() on each one. This made it easy to add both the low-balance alert and the print-balance behavior without touching the Balance class at all.

The low-balance alert fires when the balance drops below a configurable threshold, which felt like a realistic feature (like an overdraft warning from a bank app). The PrintBalanceObserver is simpler, it just prints the current balance every time it changes, which is useful for seeing what's going on when you run the app.

One thing I thought about is that if observers did slow things like sending emails or calling an external API, every transaction would block until all of them finished. For this project it's fine, but it's something to keep in mind.


Factory Method Pattern - Student Choice (IncomeTransactionFactory and ExpenseTransactionFactory)

I chose the Factory Method pattern as my fourth pattern. I picked it because every time I needed to create a transaction I had to pass in a TransactionType enum value, and it felt repetitive and easy to mix up. The factory classes wrap that detail up so you just call income_factory.create(200, "Salary") and don't have to think about the enum at all.

It also made main.py easier to read. You can tell from the variable name what kind of transaction is being created without having to look at the arguments. The trade-off is that it adds two extra classes for something that isn't that complicated. For a project this small it might be a bit much, but if the Transaction constructor got more complex in the future it would start to pay off.


General Thoughts

Going into this project I had a general idea of what design patterns were but had never actually implemented them from scratch. The Observer pattern was the one that clicked the most for me. Once I saw how cleanly you could separate the alert logic from the balance logic it made sense why people use it so much. The Singleton was the simplest conceptually but caused the most friction when writing tests, which taught me something about the real-world trade-offs that come with it. Overall I think using these patterns made the code a lot easier to follow and extend, even for a project this size.
