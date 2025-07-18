def update_signal(signals, active_signals, signal_id, status):
    signals[signal_id] = status
    active_signals.add(signal_id)
    print(f"Signal at {signal_id[0]} @ {signal_id[1]} set to {status}.")

def display_signals(signals, active_signals):
    print("\nActive Signals:")
    for signal_id in active_signals:
        status = signals.get(signal_id, "Unknown")
        print(f"{signal_id[0]} @ {signal_id[1]}: {status}")
