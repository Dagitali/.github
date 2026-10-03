// Fixture.swift — deterministic Swift runtime fixture.
//
// Responsibilities
// - Provide a tiny public API for build and test evidence.
//
// Maintainer Notes
// - Keep this independent of Xcode app tooling and external services.

/// Return the sum used by the standalone package smoke test.
public func add(_ left: Int, _ right: Int) -> Int { left + right }
