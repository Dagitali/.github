// FixtureTests.swift — Swift package smoke coverage.
//
// Responsibilities: Verify the package API is buildable and callable under
// XCTest.
//
// Maintainer Notes: No simulator, signing identity, or application host is
// required.
import XCTest
@testable import Fixture

final class FixtureTests: XCTestCase {
    func testAdd() { XCTAssertEqual(Fixture.add(2, 3), 5) }
}
