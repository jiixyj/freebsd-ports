--- happydoclib/CommandLineApp.py.orig
+++ happydoclib/CommandLineApp.py
@@ -102,10 +102,21 @@
     #
     # Exception names
     #
-    ReservedOptionName = 'Reserved option name'
-    HelpRequested='Help requested'
-    InvalidOptionValue='Invalid value for option'
-    InvalidArgument='Invalid argument to program'
+    class ReservedOptionName(ValueError):
+        'Reserved option name'
+        pass
+
+    class HelpRequested(ValueError):
+        'Help requested'
+        pass
+
+    class InvalidOptionValue(ValueError):
+        'Invalid value for option'
+        pass
+
+    class InvalidArgument(ValueError):
+        'Invalid argument to program'
+        pass
 
     #
     # Globally useful configuration stuff.
