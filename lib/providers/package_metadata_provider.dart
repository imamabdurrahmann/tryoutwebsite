import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../core/models/package_metadata.dart';

/// Provider untuk拿到 PackageMetadata dari packageId.
final packageMetadataProvider =
    Provider.family<PackageMetadata, String>((ref, packageId) {
  return PackageMetadataRepository.get(packageId);
});
