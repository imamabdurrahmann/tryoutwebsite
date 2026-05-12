// Basic smoke test for TryOutCPNS app.

import 'package:flutter_test/flutter_test.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:tryout_cpns/main.dart';

void main() {
  testWidgets('App renders smoke test', (WidgetTester tester) async {
    // Build our app with ProviderScope and trigger a frame.
    await tester.pumpWidget(
      const ProviderScope(
        child: TryOutCPNSApp(),
      ),
    );

    // Verify the app title is rendered.
    expect(find.text('TryOutCPNS'), findsOneWidget);
  });
}
